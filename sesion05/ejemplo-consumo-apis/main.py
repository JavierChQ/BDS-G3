from lib_randomuser import RandomUserApi

if __name__ == "__main__":
    api = RandomUserApi()
    results = int(input("Cuanros usuarios quiere obtener? "))
    users = api.get_users(results)
    for user in users:
        print(f"Nombe: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Telefono: {user['phone']}")
        print(f"Pais: {user['location']['country']}")
        print(f"Foto: {user['picture']['large']}")
        print("="*40)

    respuesta = input("Desea guardar los datos en la base de datos? (s/n): ")
    if respuesta.lower() == 's':
        api.insert_users_to_db(users)
        print("Datos guardados en la base de datos.")
    else:
        print("Datos no guardados.")