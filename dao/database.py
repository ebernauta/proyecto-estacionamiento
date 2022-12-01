from pymongo import MongoClient
def conexion():
    try:
        uri = "mongodb+srv://adminProyect:acceso123@sistema-estacionamiento.ieortuz.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri)
        print("Conectado a la base de datos")
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return client


