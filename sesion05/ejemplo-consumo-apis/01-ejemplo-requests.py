import requests

URL = "https://randomuser.me/api/?results=10"

response = requests.get(URL)

# print(f"Respuesta del servidor: {response.status_code}")
# print(f"Cabeceras: {response.headers}")
# print(f"Contenido: {response.json()}")

if response.status_code == 200:
    data = response.json()
    for user in data["results"]:
        print(f"Nombe: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Telefono: {user['phone']}")
        print(f"Pais: {user['location']['country']}")
        print(f"Foto: {user['picture']['large']}")
        print("="*40)
else:
    print(f"Algo esta mal {response.status_code}")