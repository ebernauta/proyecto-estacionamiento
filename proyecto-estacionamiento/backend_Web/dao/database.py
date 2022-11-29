from pymongo import MongoClient, server_api
def conexion():
    try:
        client = MongoClient("mongodb+srv://adminProyect:adminProyect@sistema-estacionamiento.ieortuz.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        print("Conectado a la base de datos")
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db

