import requests
import tkinter as tk
from tkinter import filedialog
import json
import os
import time
#version unificada para facilitar crear un solo exe
def json_variable_entorno():
    ventana = tk.Tk()
    ventana.withdraw()
    archivopath = filedialog.askopenfilename(
        title="Seleccione un archivo",
        filetypes=(("Archivos de imagen", "*.json;"), ("Todos los archivos", "*.*"))
    )
    if archivopath is None:
        return None
    else:
        with open(archivopath, "r") as archivo:
            archivostring = archivo.read()
            archivodic = json.loads(archivostring)
            access_id = archivodic.pop("access_id")
            secret_token = archivodic.pop("secret_token")
            return access_id+':'+secret_token

def crear_variable_entorno():
    variable = "COMTY_API"
    valor = json_variable_entorno()
    os.system(f'setx {variable} "{valor}"')
    print("Se va a cerrar el programa...")
    time.sleep(3)
    exit(0)
def get_variable_entorno():
    if os.getenv("COMTY_API"):
        comty_api = os.getenv("COMTY_API")
        print(comty_api)
        return True
    elif "COMTY_API" in os.environ:
        comty_api = os.environ["COMTY_API"]
        print(comty_api)
        return True
    else:
        print("No se encuentra el COMTY_API")
        return False
uploadFileUrl = "https://indev.comty.app/api/upload/file"

def upload_attachment():
    ventana = tk.Tk()
    ventana.withdraw()

    filepath = filedialog.askopenfilename(
        title="Seleccione un archivo",
        filetypes=(("Archivos de imagen y video", "*.jpg;*.png;*.gif;*.jpeg;*.mp4;"), ("Todos los archivos", "*.*"))
    )

    if not filepath:
        return None

    with open(filepath, "rb") as file:
        files = {"file": file}
        response = requests.post(uploadFileUrl, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("URL del archivo subido:", data["url"])
            print("ID del archivo:", data["id"])
            return data
        else:
            print(f"Error al subir el archivo: {response.status_code}")
            return None

def activar_boton():
    attachmentInput = attachment_entry.get().lower()  # Leer y normalizar el texto de attachment_entry
    messageInput = message_entry.get()  # Leer el texto del mensaje
    # Verificar si se desea subir un archivo
    if attachmentInput == "si" or estado_sino["boton_actual"] == "si":
        attachmentResult = upload_attachment()
        if not attachmentResult:
            errormsg = tk.Label(root, text="Error: No se ha podido subir el archivo.", font=("Arial", 14),fg="Red", background="#1e1f22")
            errormsg.pack()
            print("Error: No se ha podido subir el archivo.")
            return
        try:
            data = {
                "message": messageInput,
                "attachments": [
                attachmentResult
                ]
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                print("Item creado:", response.json())
                return
            else:
                print(f"Error al crear el item: {response.status_code}")
                return
        except Exception as e:
            print(f"Error al realizar la solicitud: {e}")
            return

    if attachmentInput == "no"or estado_sino["boton_actual"] == "no":
        try:
            data = {
                "message": messageInput,
                "attachments": [
                None
                ]
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                print("Item creado:", response.json())
                return
            else:
                print(f"Error al crear el item: {response.status_code}")
                return
        except Exception as e:
            print(f"Error al realizar la solicitud: {e}")
            return
def activar_boton_sino(estado_sino):
    if estado_sino["boton_actual"] == "si":
        estado_sino["boton_actual"] = "no"
        boton_sino.config(text=estado_sino["boton_actual"])
        boton_sino.config(background="Red")
    elif estado_sino["boton_actual"] == "no":
        estado_sino["boton_actual"] = "si"
        boton_sino.config(text=estado_sino["boton_actual"])
        boton_sino.config(background="Green")

# Configurar y verificar la variable de entorno
get_variable_entorno()
estado_sino = {"boton_actual": "no"}
if get_variable_entorno() is True:
    url = "https://indev.comty.app/api/posts/new"
    headers = {
        'Authorization': 'Server ' + os.getenv("COMTY_API")
    }
    # Configuración de la interfaz gráfica
    root = tk.Tk()
    root.title("Comty API")
    root.geometry("400x300")
    root.config(background="#1e1f22")

    # POST texto
    post_label = tk.Label(root, text="Introduzca el post", font=("Arial", 14), background="LightGray")
    post_label.pack()
    message_entry = tk.Entry(root, font=("Arial", 14), background="#3f4148")
    message_entry.pack()

    # POST archivo
    foto_label = tk.Label(root, text="¿Deseas subir un archivo (si, no)", font=("Arial", 14), background="LightGray")
    foto_label.pack()

    #Sustituido por botón sino
    attachment_entry = tk.Entry(root, font=("Arial", 14),background="#3f4148")
    attachment_entry.pack()

    # Botón sino
    boton_sino = tk.Button(root, text=estado_sino["boton_actual"],background="Red", command=lambda:activar_boton_sino(estado_sino))
    boton_sino.pack()
    # Botón de activación
    boton = tk.Button(root, text="Subir", command=activar_boton)
    boton.pack()

    # Botón de salir
    #boton_salir = tk.Button(root, text="Salir", command=root.quit).pack(pady=10)
    root.mainloop()
else:
    crear_variable_entorno()
