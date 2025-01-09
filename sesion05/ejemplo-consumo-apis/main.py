from lib_randomuser import RandomUserApi

if __name__ == "__main__":
    api = RandomUserApi()
    results = int(input("Cuanros usuarios quiere obtener? "))
    data = api.get_users(results)
    for user in data:
        print(f"Nombe: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Telefono: {user['phone']}")
        print(f"Pais: {user['location']['country']}")
        print(f"Foto: {user['picture']['large']}")
        print("="*40)