import csv

# with open("products.csv") as file:
#     print(file.read())

with open("products.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    print(list(csv_reader))
    for p in csv_reader:
        if p[2] == "False":
            print(f"ürün adı: {p[0]} fiyat: {p[1]}")

# DictReader