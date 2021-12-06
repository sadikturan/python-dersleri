import requests
from bs4 import BeautifulSoup

search_input = input('aramak istediğiniz kelime: ').replace(' ','+')
link = "https://www.google.com/search?q=" + search_input

headerParams = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

response = requests.get(link, headers = headerParams)

soup = BeautifulSoup(response.content,"html.parser")

results = soup.find_all('div', class_="rc")

for div in results:
    anchor = div.find('a')

    link = anchor['href']
    text = anchor.find('h3').string
    description = anchor.parent.next_sibling.find('span').text

    print(link + "*** " + text + "*** " + description)
    print('*******************')
