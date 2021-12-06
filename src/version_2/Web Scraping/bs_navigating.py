from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj.head
sonuc = obj.body.div.contents[1]
sonuc = obj.body.div.contents[3].contents[1]

# for child in obj.body.div.children:
#     if child != "\n":
#         print(child)

# for child in obj.body.div.descendants:
#     if child != "\n":
#         print(child)

# h2 = obj.body.h2
# div = h2.parent
# div2 = div.next_sibling.next_sibling 

ucuncu_li = obj.find(class_="ucuncu")
ikinci_li = ucuncu_li.previous_sibling.previous_sibling
birinci_li = ikinci_li.find_previous_sibling('li')
lis = ucuncu_li.find_previous_siblings('li')

ul = birinci_li.parent.parent
div = birinci_li.find_parent('div')

print(div)