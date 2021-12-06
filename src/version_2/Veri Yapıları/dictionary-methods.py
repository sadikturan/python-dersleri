opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():
#     print(x)

# for x,y in opelObj.items():
#     print(x,y)

# sonuc = "marka" in opelObj
# sonuc = len(opelObj)
# opelObj["renk"] = "kırmızı"
# opelObj.pop("renk")
# opelObj.popitem()

# del opelObj["marka"]
# del opelObj
# opelObj.clear()

obj = opelObj.copy() # referans

obj["marka"] = "Mazda"

opelObj.update({
    "marka": "Bmw",
    "renk": "Kırmızı"
})

# print(sonuc)
print(obj)
print(opelObj)