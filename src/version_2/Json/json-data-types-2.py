data = {
    "sadikturan": {
        "firstName":"Sadık",
        "lastName":"Turan"
    },
    "cinarturan": {
        "firstName":"Çınar",
        "lastName":"Turan"
    }
}

import json

with open("users2.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users2.json") as file:
    users = json.load(file)

print(users["sadikturan"])
print(users["cinarturan"])

users.update({
    "emelturan": 
        {
            "firstName": "Emel",
            "lastName": "Turan",
            "age":30
        }
})

users.pop("sadikturan")

with open("users2.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)

