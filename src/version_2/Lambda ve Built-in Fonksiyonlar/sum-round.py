sayilar = [34,2,5,7,98]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 10)

urunler = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
    {"title":"iphone 11 Pro", "price": 0},
]

# toplamFiyat = sum([urun["price"] for urun in urunler])
# sonuc = toplamFiyat / len(urunler)

toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdeti = len([urun for urun in urunler if urun["price"]>0])
sonuc = toplamFiyat / urunAdeti

sonuc = round(10.2)
sonuc = round(10.6)
sonuc = round(10.5)
sonuc = round(1.424242, 2)
sonuc = round(1.426242, 2)
sonuc = round(1.426242, 4)

print(sonuc)