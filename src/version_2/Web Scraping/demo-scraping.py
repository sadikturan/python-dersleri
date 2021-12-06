# Web Scraping: sadikturan.com

# requests ile html kaynağını alın.
# html kaynağını beautifulsoup ile yorumlayınız.
#   ** anasayfadaki kurs listesi.
#       ** kurs resmi, kurs başlığı, acıklama, udemy_link, site_link
# kurs bilgilerini kurslar.csv dosyasına kayıt et. 

import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.sadikturan.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

kurslar = soup.find_all(class_="kurs")

with open('kurslar.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['kurs_resmi','kurs_baslik','kurs_aciklama','udemy_link','site_link'])

    for kurs in kurslar:
        kurs_resmi = kurs.find('img')['src']
        kurs_basligi = kurs.find(class_="media-body").find('h2').string
        kurs_aciklama = kurs.find(class_="media-body").find('span').string
        linkler = kurs.find(class_="card-footer").find_all('div')[1].find_all('a')
        kurs_udemy_link = linkler[0]['href']
        kurs_site_link = url + linkler[1]['href']

        csv_writer.writerow([kurs_resmi,kurs_basligi,kurs_aciklama,kurs_udemy_link,kurs_site_link])

