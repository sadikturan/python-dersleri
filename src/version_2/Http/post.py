import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
        "title": 'deneme',
        "body": 'deneme',
        "userId": 1,
    }
)

sonuc = response
sonuc = response.text
sonuc = response.json()
sonuc = response.headers

print(sonuc)