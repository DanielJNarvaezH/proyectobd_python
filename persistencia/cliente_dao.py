from conexion_oracle import obtener_conexion

class ClienteDAO:
    """Clase DAO para manejar la tabla T_CLIENTES"""

    def insertar_cliente(self, nombre, apellido, cedula, direccion, telefono, email, estado):
        conn = obtener_conexion()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            # Usamos la secuencia seq_clientes para generar el ID automáticamente
            sql = """
                INSERT INTO T_CLIENTES
                VALUES (seq_clientes.NEXTVAL, :1, :2, :3, :4, :5, :6, :7)
            """
            cur.execute(sql, (nombre, apellido, cedula, direccion, telefono, email, estado))
            conn.commit()
            print("✅ Cliente insertado correctamente.")
        except Exception as e:
            print("❌ Error al insertar cliente:", e)
            conn.rollback()
        finally:
            conn.close()

    def listar_clientes(self):
        conn = obtener_conexion()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            cur.execute("SELECT Cl_id, Cl_nombre, Cl_apellido, Cl_email, Cl_estado FROM T_Clientes")
            clientes = cur.fetchall()

            print("\n📋 Lista de clientes:")
            for c in clientes:
                print(f"ID: {c[0]}, Nombre: {c[1]} {c[2]}, Email: {c[3]}, Estado: {c[4]}")
        except Exception as e:
            print("❌ Error al listar clientes:", e)
        finally:
            conn.close()
