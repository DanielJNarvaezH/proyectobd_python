import oracledb

# Credenciales y datos de conexión
user = "tienda"
password = "tienda123"
dsn = "localhost:1521/XEPDB1"  # Formato: host:puerto/servicename

try:
    # Conectarse a Oracle
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
    print("✅ Conexión exitosa con el usuario 'tienda'")

    # Ejecutar una consulta simple
    cur = conn.cursor()
    cur.execute("SELECT sysdate FROM dual")
    for row in cur:
        print("Fecha del servidor Oracle:", row[0])

except Exception as e:
    print("❌ Error al conectar con Oracle:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("🔒 Conexión cerrada")
