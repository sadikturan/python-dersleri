# urunAdi, fiyat, satistami ve kategori bilgilerini alarak json veri türünde kayıt yapan fonksiyon.
# ürün bilgilerini getiren fonksiyon.

def urunEkle(urunAdi,fiyat,satistami,kategoriler):
    urun = {
        "urunAdi": urunAdi,
        "fiyat": fiyat,
        "satistami": satistami,
        "kategoriler": kategoriler
    }

    import json
    with open("urunler.json","w") as file:
        json.dump(urun, file, ensure_ascii=False)

# urunEkle("iphone 12",8000,True,["telefon","elektronik"])

def urunleriGetir():
    import json
    with open("urunler.json") as file:
        urun = json.load(file)

    kategoriler = ' '.join([kategori for kategori in urun["kategoriler"]]
    print(kategoriler)
    print(f'ürün adı: {urun["urunAdi"]} fiyat: {urun["fiyat"]} kategoriler: {kategoriler}')

urunleriGetir()

