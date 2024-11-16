import requests
import os

hostname = "https://indev.comty.app/api"
headers = {
    'Authorization': os.getenv("COMTY_API")
}


def get_other_userid(username):
    url_user_id = "https://indev.comty.app/api/users/" + username + "/resolve-user_id"
    print(url_user_id)
    user_id = requests.get(url_user_id).json()
    actual_id = user_id["user_id"]
    return actual_id


def get_self_userdata():
    user_data = requests.get(hostname + "/users/self", headers=headers).json()
    return user_data


def create_post(message, attachment):
    if attachment is None:
        data = {
            "message": message,
        }
    elif attachment is not None:
        data = {
            "message": message,
            "attachments": [attachment]
        }
    response = requests.post(hostname + "/posts/new", json=data, headers=headers)
    if response.status_code == 200:
        print("Item creado:", response.json())
        return
    else:
        print(f"Error al crear el item: {response.status_code}", "\nIbas a publicar: ", response.json())
        return


def upload_attachment(files):
    response = requests.post(hostname + "/upload/file", files=files, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("URL del archivo subido:", data["url"])
        print("ID del archivo:", data["id"])
        return data
    else:
        print(f"Error al subir el archivo: {response.status_code}")
        return None


def get_post():
    response = requests.get(hostname + "/posts/feed/global")  # Hacer la petición GET
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta a JSON
        for post in data:
            print(f"Usuario: {post['user']['username']}", )
            print(f"Mensaje: {post['message']}")

        print(data)
    else:
        print(f"Error: {response.status_code}")
