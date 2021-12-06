from csv import DictReader

with open("products.csv") as file:
    csv_reader = DictReader(file)
    for p in csv_reader:
        if (p["Category"] == "Bilgisayar"):
            print(p['ProductName'],p['Price'])