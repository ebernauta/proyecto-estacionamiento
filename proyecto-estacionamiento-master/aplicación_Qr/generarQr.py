"""import qrcode
img = qrcode.make("RT-TC-51")

img.save("Patente.png")"""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['Usuarios']

colAlumnos = db['Alumnos']

"""coleccion.insert_one({
    'nombre': 'salvador',
    'rut': '12345678-9',
    'numeroTelefonico': '123456789',
    'patente': 'RT-TC-51',
    'carrera': 'Ingenieria Civil Informatica',
    'horarioClases': 'diurno',
})
"""
#patente = {'patente':'RT-TC-51'} --> Probando dentro de una variable

#Te muestra los datos que contiene dentro de la coleccion
for datos in colAlumnos.find({'patente':'RT-TC-51'},{'nombre':0,'rut':0, '_id':0, 'numeroTelefonico':0, 'carrera':0, 'horarioClases':0}):
    print(datos)


#Basicamente eligo si quiero mostrar la clave o el valor llamando datos.items() 
for key, value in datos.items():
    print(value) #--> Muestra SOLO el valor de la clave
    print(key) #--> Muestra SOLO la clave

print(db.list_collection_names())


"""
nombre = 'salvador'
coleccion.insert_one({
    'nombre': ""+nombre+"",
    'rut': '12345678-9',
    'numeroTelefonico': '123456789',
    'patente': 'RT-TC-51',
    'carrera': 'Ingenieria Civil Informatica',
    'horarioClases': 'diurno',})"""