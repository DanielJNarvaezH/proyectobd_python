import oracledb

def obtener_conexion():
    try:
        connection = oracledb.connect(
            user="tienda",
            password="tienda123",
            dsn="localhost:1521/XEPDB1"
        )
        return connection
    except Exception as e:
        print("❌ Error al conectar con Oracle:", e)
        return None
