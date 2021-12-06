# url?key1=value1&key2=value2

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos?completed=true&userId=1")
response = requests.get("https://jsonplaceholder.typicode.com/todos", params={
    "userId":1,
    "completed":"true"
})
liste = response.json()


print(liste[0]["title"])