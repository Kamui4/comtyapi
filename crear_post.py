import requests
from subir_archivo import upload_attachment
import os
url = "https://indev.comty.app/api/posts/new"
headers = {
    'Authorization':'Server '+os.getenv("COMTY_API")
}
print(headers)
data = None
salir = False
while not salir:
    messageInput = input("¿Que deseas publicar?")
    attachmentInput = input("¿Deseas subir un archivo(si,no)?")

    if attachmentInput == "si":
        attachmentResult = upload_attachment()
        try:
            data = {
                "message": messageInput,
                "attachments": [
                    attachmentResult,
                ]
            }
        except Exception as err:
            raise ValueError("Agregue un archivo porfavor, error 1")

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