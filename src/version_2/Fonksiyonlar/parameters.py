def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("Sadık")
sonuc = selamla("Yağmur")

def toplam(a,b):
    return a + b

sonuc = toplam(10,20)
sonuc = toplam(20,30)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

sonuc = yasHesapla(1983)
sonuc = yasHesapla(1993)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz.")

emekliligeKacYilKaldi(1983, "Sadık")
emekliligeKacYilKaldi(1950, "Ali")