import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="mi_base_de_datos"
)
cursor = conn.cursor()

# Insertar un registro de forma segura (create)
try:
    sql = "INSERT INTO mi_tabla (nombre, edad, ciudad) VALUES (%s, %s, %s)"
    val = ("Ejemplo", 30, "Ejemplo City")
    cursor.execute(sql, val)
    conn.commit()
    print("Registro insertado con éxito")
except Exception as e:
    print("Error al insertar registro:", e)
finally:
    cursor.close()
    conn.close()

# Leer un registro de forma segura
try:
    sql = "SELECT * FROM mi_tabla WHERE id = %s"
    val = (1,)  # ID del registro a leer
    cursor.execute(sql, val)
    resultado = cursor.fetchone()
    print(resultado)
except Exception as e:
    print("Error al leer registro:", e)
finally:
    cursor.close()
    conn.close()

# Leer varios registros de forma segura (read)
try:
    sql = "SELECT * FROM mi_tabla WHERE edad >= %s"
    val = (25,)  # Edad mínima
    cursor.execute(sql, val)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
except Exception as e:
    print("Error al leer registros:", e)
finally:
    cursor.close()
    conn.close()

# Actualizar un registro de forma segura (update)
try:
    sql = "UPDATE mi_tabla SET edad = %s WHERE nombre = %s"
    val = (35, "Ejemplo")
    cursor.execute(sql, val)
    conn.commit()
    print("Registro actualizado con éxito")
except Exception as e:
    print("Error al actualizar registro:", e)
finally:
    cursor.close()
    conn.close()

# Eliminar un registro de forma segura (delete)
try:
    sql = "DELETE FROM mi_tabla WHERE nombre = %s"
    val = ("Ejemplo",)
    cursor.execute(sql, val)
    conn.commit()
    print("Registro eliminado con éxito")
except Exception as e:
    print("Error al eliminar registro:", e)
finally:
    cursor.close()
    conn.close()
