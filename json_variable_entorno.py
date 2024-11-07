import tkinter as tk
from tkinter import filedialog
import json
import os
import time

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
    perm = input("¿Desea crear una variable persistente?(si,no)")
    match perm:
        case "si":
            variable = "COMTY_API"
            valor = json_variable_entorno()
            os.system(f'setx {variable} "{valor}"')
            print("Se va a cerrar el programa...")
            time.sleep(3)
            exit(0)
        case "no":
            os.environ["COMTY_API"] = json_variable_entorno()
        case _:
            print("Introduzca una respuesta válida")

def get_variable_entorno():
    if os.getenv("COMTY_API"):
        comty_api = os.getenv("COMTY_API")
        print(comty_api)
    elif "COMTY_API" in os.environ:
        comty_api = os.environ["COMTY_API"]
        print(comty_api)
    else:
        print("No se encuentra el COMTY_API")
crear_variable_entorno()