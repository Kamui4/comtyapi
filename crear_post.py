import requests
from subir_archivo import upload_attachment
from json_variable_entorno import get_variable_entorno,crear_variable_entorno
import os
import tkinter
import time
messageInput = None
attachmentInput = None
def activar_boton():
    attachmentInput = attachment_entry.get().lower()  # Leer y normalizar el texto de attachment_entry
    messageInput = message_entry.get()  # Leer el texto del mensaje

    # Verificar si se desea subir un archivo
    if attachmentInput == "si":
        attachmentResult = upload_attachment()
        if attachmentResult is None:
            errormsg = tkinter.Label(root, text="Error: No se ha podido subir el archivo.", font=("Arial", 14), fg="Red",background="#1e1f22")
            errormsg.pack()
            print("Error: No se ha podido subir el archivo.")

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
            else:
                print(f"Error al crear el item: {response.status_code}")
        except Exception as e:
            print(f"Error al realizar la solicitud: {e}")

    if attachmentInput == "no":
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
            else:
                print(f"Error al crear el item: {response.status_code}")
        except Exception as e:
            print(f"Error al realizar la solicitud: {e}")



if get_variable_entorno() is True:
    url = "https://indev.comty.app/api/posts/new"
    headers = {
        'Authorization': 'Server ' + os.getenv("COMTY_API")
    }
    data = None
    salir = False
    # interfaz grafica
    root = tkinter.Tk()
    root.title("Comty API")
    root.geometry("800x800")
    root.config(background="#1e1f22")
    # POST texto
    post_label = tkinter.Label(root, text="Introduzca el post", font=("Arial", 14), background="LightGray")
    post_label.pack()
    message_entry = tkinter.Entry(root, font=("Arial", 14))
    message_entry.pack()
    #POST foto
    foto_label = tkinter.Label(root, text="¿Deseas subir un archivo(si,no)", font=("Arial", 14), background="LightGray")
    foto_label.pack()
    attachment_entry = tkinter.Entry(root, font=("Arial", 14))
    attachment_entry.pack()
    #BOTON
    boton = tkinter.Button(root, text="Subir",command=lambda:activar_boton())
    boton.pack()

    """#BOTON SI
    attachmentInputSI = tkinter.Button(text="SI", font=("Arial", 14), background="Green", command=lambda:boton_si(url,headers))
    attachmentInputSI.pack()
    #BOTON NO
    attachmentInputNO = tkinter.Button(text="NO", font=("Arial", 14), background="Red", command=lambda:boton_no(url,headers))
    attachmentInputNO.pack()"""

    # messageInput = input("¿Que deseas publicar?")
    # attachmentInput = input("¿Deseas subir un archivo(si,no)?")

    root.mainloop()

elif get_variable_entorno() is False:
    crear_variable_entorno()