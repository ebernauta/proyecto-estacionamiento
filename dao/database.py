from pymongo import MongoClient
def conexion():
    try:
        client = MongoClient("mongodb+srv://adminProyect:acceso123@sistema-estacionamiento.ieortuz.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        print("Conectado a la base de datos")
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db