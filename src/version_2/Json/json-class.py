class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = Product("Samsung S10",5000)
p2 = Product("Samsung S11",6000)

products = [p1.__dict__,p2.__dict__]

import json

with open("urunler.json","w") as file:
    json.dump(products,file)

with open("urunler.json") as file:
    data = json.load(file)

urunler = []

for p in data:
    urunler.append(Product(p["name"],p["price"]))

    
