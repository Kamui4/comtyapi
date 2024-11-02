import requests
import tkinter as tk
from tkinter import filedialog

uploadFileUrl = "https://indev.comty.app/api/upload/file"
headers = {
    "Authorization":"Server 31aaa395-22f5-4528-9406-38dc0e05d21e:gQmpSd5dr8WS1hi7GsufY6lBceII5ZYK7b8Q",
    "use-compression": "false",
}

def upload_attachment():
    ventana = tk.Tk()
    ventana.withdraw()

    filepath = filedialog.askopenfilename(
        title="Seleccione un archivo",
        filetypes=(("Archivos de imagen", "*.jpg;*.png;*.gif;*.jpeg;*.mp4;"), ("Todos los archivos", "*.*"))
    )

    if filepath is None:
        return None

    with open(filepath, "rb") as file:
        files = {
            "file": file
        }

        response = requests.post(uploadFileUrl, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()

            print("URL del archivo subido:", data["url"])
            print("ID del archivo:", data["id"])

            return data
        else:
            return None