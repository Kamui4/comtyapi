import requests
from subir_archivo import upload_attachment

url = "https://indev.comty.app/api/posts/new"
headers = {
    "Authorization":"Server 31aaa395-22f5-4528-9406-38dc0e05d21e:gQmpSd5dr8WS1hi7GsufY6lBceII5ZYK7b8Q"
}

salir = False
while not salir:
    messageInput = input("¿Que deseas publicar?")
    attachmentInput = input("¿Deseas subir un archivo?")

    if attachmentInput == "si":
        attachmentResult = upload_attachment()

    data = {
        "message": messageInput,
        "attachments": [
            attachmentResult,
        ]
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