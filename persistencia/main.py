from cliente_dao import ClienteDAO

if __name__ == "__main__":
    dao = ClienteDAO()

    # Insertar un cliente de prueba
    dao.insertar_cliente(
        nombre="Carlos",
        apellido="Ramírez",
        cedula="1122334455",
        direccion="Av. Siempre Viva 742",
        telefono="3024567890",
        email="carlos@mail.com",
        estado="activo"
    )

    # Listar todos los clientes
    dao.listar_clientes()
