import requests
import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccione un archivo",
        filetypes=(("Archivos de imagen", "*.jpg;*.png;*.gif;*.jpeg;"), ("Todos los archivos", "*.*"))
    )

    if ruta_archivo:
        print("Ruta seleccionada:", ruta_archivo)
        return ruta_archivo
    else:
        return None

headers = {
        "Authorization":"Server 31aaa395-22f5-4528-9406-38dc0e05d21e:gQmpSd5dr8WS1hi7GsufY6lBceII5ZYK7b8Q"
    }
url = "https://indev.comty.app/api/upload/file"
ventana = tk.Tk()
ventana.withdraw()  # Ocultar la ventana principal de Tkinter
# Abrimos el archivo en modo binario para la carga
with open(seleccionar_archivo(), "rb") as file:
    # Crear el diccionario para el campo 'file'
    files = {
        "file": file
    }

    # Realizar la petición POST
    response = requests.post(url, files=files, headers=headers)

    # Verificar si la petición fue exitosa (código 200)
    if response.status_code == 200:
        # Convertir la respuesta en JSON
        data = response.json()
        print("URL del archivo subido:", data["url"])
        print("ID del archivo:", data["id"])
    else:
        print(f"Error al cargar el archivo: {response.status_code}")
        print(response.text)



