import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

sonuc = response
sonuc = type(response)
sonuc = response.status_code
sonuc = response.headers
sonuc = response.headers["Content-Type"]
sonuc = response.url
sonuc = response.encoding
sonuc = response.text
todos = json.loads(response.text)
sonuc = todos[0]["title"]

for item in todos:
    if (item["userId"]==1):
        print(item["title"])

print(sonuc)