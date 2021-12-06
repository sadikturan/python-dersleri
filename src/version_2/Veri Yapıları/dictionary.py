# key - value

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index('istanbul')])
# print(plakalar[sehirler.index('kocaeli')])

plakalar = {'kocaeli': 41,'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

plakalar['rize'] = 53
# plakalar['izmir'] = 36

# plakalar['izmir'] = 35 # 36 to 35
# print(plakalar)

ogrenciler = { 
    100: {
        "ad": "Çınar",
        "soyad": "Turan",
        "yas": 4,
        "notlar": [70,80,70]
    }, 
    101: {
        "ad": "Ada",
        "soyad": "Bilgi",
        "yas": 10
    } 
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[101]["ad"]
sonuc = ogrenciler[101]["soyad"]

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)

