# no vs filedialog en linux


from pathlib import Path
from PIL import ImageTk, Image
import ctypes
import requests
import json
import os
import time
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Text, Button, PhotoImage, END, Label,messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\sergi\PycharmProjects\build\assets\frame0")

def closing_cbk(): #para terminar el programa cuando se cierra la ventana
    # Shutdown procedure
    window.quit()
    window.destroy()
#funcion de tkinter designer
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
#funcion del texto con placeholder
def on_focus_in(event):
    if message_entry.get("1.0", END).strip() == placeholder_text:
        message_entry.delete("1.0", END)
        message_entry.config(fg='#9a9a9a')

def on_focus_out(event):
    if message_entry.get("1.0", END).strip() == '':
        message_entry.insert("1.0", placeholder_text)
        message_entry.config(fg='grey')
def obtener_texto():
    # Obtiene el texto desde el principio (1.0) hasta el final (END)
    texto = message_entry.get("1.0", END)
    return texto.strip()  # Imprime el texto sin espacios en blanco al final

#FUNCIONES DE LA API
def json_variable_entorno():
    ventana = Tk()
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
    valor = "Server "+json_variable_entorno()
    os.system(f'setx {variable} "{valor}"')
    print("Se va a cerrar el programa...")
    time.sleep(3)
    sys.exit(0)

def get_variable_entorno():
    if os.getenv("COMTY_API"):
        comty_api = os.getenv("COMTY_API")
        print(comty_api)
        return True
    else:
        print("No se encuentra el COMTY_API")
        return False

def seleccionar_archivo():
    try:
        # Llamar a zenity para abrir un cuadro de diálogo de selección de archivo
        resultado = subprocess.run(
            ["zenity", "--file-selection", "--title=Seleccione un archivo"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Verificar si el usuario canceló el diálogo
        if resultado.returncode != 0:
            print("Selección de archivo cancelada.")
            return None

        # Obtener la ruta del archivo seleccionado
        filepath = resultado.stdout.strip()
        print("Archivo seleccionado:", filepath)
        return filepath

    except Exception as e:
        print(f"Error al seleccionar archivo: {e}")
        return None

def upload_attachment():
    upload_file_url = "https://indev.comty.app/api/upload/file"
    filepath = seleccionar_archivo()

    if not filepath:
        return None

    with open(filepath, "rb") as file:
        files = {"file": file}
        response = requests.post(upload_file_url, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("URL del archivo subido:", data["url"])
            print("ID del archivo:", data["id"])

            # Cargar y actualizar la imagen en el widget Canvas
            update_image(filepath)  # Llama a la función para actualizar la imagen en el Canvas

            return data
        else:
            print(f"Error al subir el archivo: {response.status_code}")
            messagebox.showerror("Error", "No se pudo subir el archivo.")
            return None

#ACTUALIZAR IMAGEN
def update_image(filepath):
    """Actualiza `image_1` en el Canvas con la imagen seleccionada."""
    try:
        # Cargar y redimensionar la nueva imagen
        new_image = Image.open(filepath)
        new_image = new_image.resize((150, 150))  # Ajusta el tamaño según sea necesario
        new_image_photo = ImageTk.PhotoImage(new_image)

        # Configurar `image_1` con la nueva imagen
        canvas.itemconfig(image_1, image=new_image_photo)

        # Mantener una referencia a la nueva imagen para evitar que sea eliminada por el recolector de basura
        canvas.image = new_image_photo

    except Exception as e:
        print(f"Error al actualizar la imagen: {e}")
        messagebox.showerror("Error", "No se pudo actualizar la imagen.")


def boton_upload():
    url = "https://indev.comty.app/api/posts/new"
    #attachmentInput = attachment_entry.get().lower()  # Leer y normalizar el texto de attachment_entry
    try:
        data = {
            "message": obtener_texto(),
            "attachments": [
                temporal["attachment"]
            ]
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("Item creado:", response.json())
            return
        else:
            print(f"Error al crear el item: {response.status_code}","\nIbas a publicar: ",response.json())
            return
    except Exception as e:
        print(f"Error al realizar la solicitud: {e}")
        return

def image_boton():
    # Verificar si se desea subir un archivo
    if estado_upload["boton_actual"] == "si":
        temporal['attachment'] = None
        estado_upload["boton_actual"] = "no"
        boton_archivo.config(text=estado_upload["boton_actual"])
        return
    elif estado_upload["boton_actual"] == "no":
        attachmentResult = upload_attachment()
        if not attachmentResult:
            errormsg = Label(window, text="Error: No se ha podido subir el archivo.", font=("Arial", 14), fg="Red",background="#1e1f22")
            errormsg.pack()
            print("Error: No se ha podido subir el archivo.")
            return

        temporal['attachment'] = attachmentResult
        estado_upload["boton_actual"] = "si"
        boton_archivo.config(text=estado_upload["boton_actual"])
        return


# Configurar y verificar la variable de entorno
get_variable_entorno()
placeholder_text = "Escribe aquí..."  # Texto del placeholder
temporal = {'attachment':None}
#Datos estados iniciales y datos
attachmentResult = None
estado_upload = {"boton_actual": "no"}
if get_variable_entorno() is True:
    headers = {
        'Authorization': os.getenv("COMTY_API")
    }
    window = Tk()
    window.title("Comty API")
    window.geometry("700x530")
    window.configure(bg="#232323")
    # ICONO PLACEHOLDER
    myappid = 'ddxdxdxdxd'  # string arbitrario
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    window.iconbitmap("comty.ico")

    canvas = Canvas(
        window,
        bg="#232323",
        height=700,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(
        file="button_1.png")
    boton_archivo = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: image_boton(),
        relief="flat",
        background="#353535",
        activebackground="#353535"
    )
    boton_archivo.place(
        x=91.0,
        y=198.0,
        width=25.0,
        height=25.0
    )

    button_image_2 = PhotoImage(
        file="button_2.png")
    boton = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: boton_upload(),
        relief="flat",
        background="#353535",
        activebackground="#353535"
    )
    boton.place(
        x=604.0,
        y=68.0,
        width=27.0,
        height=27.0
    )

    entry_image_1 = PhotoImage(
        file="Rectangle1.png")  # "entry_1.png"
    entry_bg_1 = canvas.create_image(
        358.5,  # 358.5
        145.5,  # 145.5
        image=entry_image_1
    )

    message_entry = Text(window, height=10, width=40, fg='grey', bg="#353535", bd=0, highlightthickness=0,
                       font=("Beiruti Regular", 16 * -1))
    message_entry.insert("1.0", placeholder_text)

    message_entry.bind("<FocusIn>", on_focus_in)
    message_entry.bind("<FocusOut>", on_focus_out)

    message_entry.place(

        x=123.0,
        y=68.0,  # 68
        width=471.0,  # 471
        height=153.0  # 153
    )

    image_image_1 = PhotoImage(
        file="placeholder.png")
    image_1 = canvas.create_image(
        140.0,
        379.0,
        image=image_image_1
    )
    window.protocol("WM_DELETE_WINDOW", closing_cbk) #para terminar el programa cuando se cierra la ventana
    window.resizable(False, False)
    window.mainloop()
else:
    crear_variable_entorno()