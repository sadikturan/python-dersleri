data = [
    {
        "userName": "sadikturan",
        "firstName": "Sadık",
        "lastName": "Turan"
    },
     {
        "userName": "cinarturan",
        "firstName": "Çınar",
        "lastName": "Turan"
    }
]

import json

user = {
        "userName": "emelturan",
        "firstName": "Emel",
        "lastName": "Turan"
}

with open("users.json") as file:
    users = json.load(file)

for user in users:
    if user["userName"] == "sadik_turan":
        user["userName"] = "sadikturan"

users.remove(users[0])

# users.append(user)

with open("users.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)
