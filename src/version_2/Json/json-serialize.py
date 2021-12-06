# serialize
import json

person = {
  "firstName": "Sadık",
  "lastName": "Turan",
  "hobbies": [
    "spor",
    "sinema"
  ],
  "age": 37,
  "children": [
    {
      "firstName": "Çınar",
      "age": 3
    }
  ]
}

print(person)
print(person["firstName"])
print(type(person))

# sonuc = json.dumps(person, ensure_ascii=False,indent=2)

# print(sonuc)
# print(type(sonuc))

with open("person.json","w") as file:
    json.dump(person,file, ensure_ascii=False,indent=2)

