from models.database import obtener_conexion

def guardar_huesped(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS huespedes (id INTEGER PRIMARY KEY, nombre TEXT)")
    cursor.execute("INSERT INTO huespedes (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()