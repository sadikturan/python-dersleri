from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()


obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj
sonuc = obj.prettify()
sonuc = type(obj)
sonuc = obj.title
sonuc = type(obj.title)
sonuc = obj.title.name
sonuc = obj.title.string

sonuc = obj.body
sonuc = obj.body.h1
sonuc = obj.h1
sonuc = obj.h1.name
sonuc = obj.h1.string

sonuc = obj.div
sonuc = obj.h2
sonuc = obj.ul
sonuc = obj.ul.li



print(sonuc)