import requests
#GET api
url = "https://indev.comty.app/api/posts/feed/global"

response = requests.get(url)  # Hacer la petición GET
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta a JSON
    for post in data:
        print(f"Usuario: {post['user']['username']}",)
        print(f"Mensaje: {post['message']}")

    print(data)
else:
    print(f"Error: {response.status_code}")