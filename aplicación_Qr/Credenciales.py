import imp
import cv2, numpy as np
from pyzbar.pyzbar import decode

#Esto detecta la camara
cap = cv2.VideoCapture(0)

# ancho de la camara
cap.set(3, 640) # 3 es la ubicacion y 640 es el ancho

#altura de la camara
cap.set(4, 480) # 4 es la ubicacion y 480 es la altura

# Se lee el archivo credenciales.txt que contiene los codigos de acceso
with open('aplicación_Qr\credenciales.txt') as f:
    #Las lineas de codigo se guardaran en un arreglo
    myDataList = f.read().splitlines()

#printear los codigos de acceso
print(myDataList)

while True:
    #Se guarda la imagen de la camara
    success, img = cap.read()
    
    
    #Detectar los codigos de barras en la imagen
    for barcode in decode(img):
        #se decodifica el codigo de barcode
        myData = barcode.data.decode('utf-8')
        
        #Se imprime el codigo
        print(myData)
        
        #Si el codigo esta en la lista de accesos 
        if myData in myDataList:
            #Se imprime el mensaje de acceso permitido
            myOutput = 'Acceso Permitido'
            color = (0, 255, 0) #Codigo de color verde
        else:
            myOutput = 'No Autorizado'
            color = (0, 0, 255) #Codigo de color Rojo
        
        #Las coordenadas del barcode    
        pts = np.array([barcode.polygon], np.int32)
        
        #Se modifica el arreglo de pts
        pts = pts.reshape((-1, 1, 2))
        
        #Se crea el cuadro de color segun el estado (Aprobado o no)
        cv2.polylines(img, #Imagen
                      [pts], #Las coordenadas
                      True, #eL cuadro es cerrado
                      color, #Color del cuadro
                      5) #El grosor del cuadro
        
        #Se da forma de un segundo cuadro para el texto
        pts2 = barcode.rect
        
        #Se va a color el texto en el cuadro
        cv2.putText(img, #Imagen
                    myOutput, #Texto
                    (pts2[0], pts2[1]), #Coordenadas
                    cv2.FONT_HERSHEY_SIMPLEX, #Tipo de letra
                    0.9, #tamaño de la letra
                    color, #Color de la letra
                    3) #Grosor de la letra
            
        
    #Se muestra la imagen
    cv2.imshow('Result', img)
    
    #Se espera un ms para terminar la camara
    cv2.waitKey(1)
        