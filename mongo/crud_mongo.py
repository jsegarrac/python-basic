import pymongo

# Conexión a la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mi_base_de_datos"]
collection = db["mi_coleccion"]

# Insertar un documento de forma segura (create)
documento = {"nombre": "Ejemplo", "edad": 30, "ciudad": "Ejemplo City"}
try:
    resultado = collection.insert_one(documento)
    print("ID del documento insertado:", resultado.inserted_id)
except Exception as e:
    print("Error al insertar:", e)


# Leer un documento por ID de forma segura (read)
try:
    documento = collection.find_one({"_id": resultado.inserted_id})
    print(documento)
except Exception as e:
    print("Error al leer:", e)

# Leer varios documentos de forma segura
try:
    documentos = collection.find({"edad": {"$gte": 25}})
    for doc in documentos:
        print(doc)
except Exception as e:
    print("Error al leer:", e)


# Actualizar un documento de forma segura (update)
query = {"nombre": "Ejemplo"}
nuevos_valores = {"$set": {"edad": 35}}
try:
    collection.update_one(query, nuevos_valores)
except Exception as e:
    print("Error al actualizar:", e)

# Actualizar varios documentos de forma segura
query = {"edad": {"$gte": 40}}
nuevos_valores = {"$set": {"ciudad": "Nueva Ciudad"}}
try:
    collection.update_many(query, nuevos_valores)
except Exception as e:
    print("Error al actualizar:", e)

# Eliminar un documento de forma segura
query = {"nombre": "Ejemplo"}
try:
    collection.delete_one(query)
except Exception as e:
    print("Error al eliminar:", e)

# Eliminar varios documentos de forma segura (delete)
query = {"edad": {"$gte": 60}}
try:
    collection.delete_many(query)
except Exception as e:
    print("Error al eliminar:", e)
