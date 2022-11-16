from pymongo import MongoClient

def conexion():
    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client['Usuarios']
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db