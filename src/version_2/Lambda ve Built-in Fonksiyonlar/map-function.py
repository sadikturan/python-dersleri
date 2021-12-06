sayilar = [1,-2,5,-7,-9]
str_sayilar = ["1","2","5","7","9"]
isimler = ["ali","deniz","emel","Çınar"]
kullanicilar = [
    {"ad": "ali", "soyad":"Yılmaz"},
    {"ad": "ahmet", "soyad":"Yılmaz"}
]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)

# def kareAl(sayi):
#     return sayi ** 2

sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
sonuc = list(map(int, str_sayilar))
sonuc = list(map(abs, sayilar))
sonuc = list(map(float, sayilar))
sonuc = list(map(len, isimler))
sonuc = list(map(str.capitalize, isimler))
sonuc = list(map(str.lower, isimler))
sonuc = list(map(lambda x: x["ad"], kullanicilar))

print(sonuc)
