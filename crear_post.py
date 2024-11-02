import requests
import time
salir = False
while not salir:
    access_id = "31aaa395-22f5-4528-9406-38dc0e05d21e"
    secret_token = "gQmpSd5dr8WS1hi7GsufY6lBceII5ZYK7b8Q"

    url = "https://indev.comty.app/api/posts/new"

    data = {
        "message": input("¿Que deseas publicar?"),
        "attachments": [
            {"url" : str(input("Introduzca link de la imagen: "))}
        ]
    }
    headers = {
        "Authorization":"Server 31aaa395-22f5-4528-9406-38dc0e05d21e:gQmpSd5dr8WS1hi7GsufY6lBceII5ZYK7b8Q"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Item creado:", response.json())
    else:
        print(f"Error: {response.status_code}")

    comprobacion = input("¿Desea seguir publicando?(si,no)")
    if comprobacion == "si":
        salir = False
    elif comprobacion == "no":
        salir = True
    else:
        salir = True

