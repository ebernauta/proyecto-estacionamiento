from base64 import encode
import importlib
import cv2, numpy as np
from pyzbar.pyzbar import decode
from flask import Flask, render_template, Response
import io

app = Flask(__name__)
cap = cv2.VideoCapture(0)
cap.set(3, 640) # 3 es la ubicacion y 640 es el ancho
cap.set(4, 480) # 4 es la ubicacion y 480 es la altura
font = cv2.FONT_HERSHEY_SIMPLEX

with open(r'C:\DEV\proyecto-estacionamiento\aplicación_Qr\credenciales.txt') as f:
    myDataList = f.read().splitlines()
print(myDataList)

def generate():
    while (True):
        ret, img = cap.read()
        for barcode in decode(img):
            mydata=barcode.data.decode('utf-8')
            print(mydata)
            (flag, encodedImage) = cv2.imencode(".jpg", img)
            pts=np.array([barcode.polygon], np.int32)
            pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
            cv2.putText(img, 'APP ESTACIONAMIENTOS',(50, 50),font, 1, (0, 255, 255), 2, cv2.LINE_4)  
            if not flag:
                continue
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                  bytearray(encodedImage) + b'\r\n')
            
        # success, img = cap.read()    
        # for barcode in decode(img):
        #     myData = barcode.data.decode('utf-8')
        #     #print(myData)
        #     if myData in myDataList:
        #         myOutput = 'Acceso Permitido'
        #         color = (0, 255, 0) #Codigo de color verde
        #     else:
        #         myOutput = 'No Autorizado'
        #         color = (0, 0, 255) #Codigo de color Rojo
        #     #yield para que se muestre en la pagina
        #     yield(b'--frame\r\n'b'Content-Type: image/jpeg\r' + b'\r\n' + cv2.imencode('.jpg', img)[1].tobytes() + b'\r\n')
        #     pts = np.array([barcode.polygon], np.int32)
        #     pts = pts.reshape((-1, 1, 2))
        #     cv2.polylines(img,[pts],True, color,5) #El grosor del cuadro
        #     pts2 = barcode.rect
        #     cv2.putText(img,myOutput,(pts2[0], pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 3)

# def camera():
#     while (True):
#         ret, img = cap.read()
#         cv2.imshow('frame', img)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    #CREAO QUE ACÁ FALTÓ EL YIELD PARA CONVERTIRLO AL FOMRATO WEB
    
def gen():
    while True:
        read_return_code, frame = cap.read()
        encode_return_code, image_buffer = cv2.imencode('.jpg', frame)
        for barcode in decode(frame):
            mydata=barcode.data.decode('utf-8')
            print(mydata)
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            pts=np.array([barcode.polygon], np.int32)
            pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 5)
            cv2.putText(frame, 'APP ESTACIONAMIENTOS',(50, 50),font, 1, (0, 255, 255), 2, cv2.LINE_4)  
                    
        io_buf = io.BytesIO(image_buffer)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + io_buf.read() + b'\r\n')

    
    
    
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(debug=True)

cap.release()