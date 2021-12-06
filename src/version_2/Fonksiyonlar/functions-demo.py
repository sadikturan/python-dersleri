# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

# def yazdir(txt, adet):
#     print(txt * adet)

# yazdir('Merhaba\n', 5)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

# def hesapla(kisa, uzun):
#     alan = kisa * uzun
#     cevre = 2 * (kisa + uzun)

#     return f"alan: {alan} çevre: {cevre}"

# print(hesapla(5,7))

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)


# def yaziTuraAt():
#     import random
#     sayi = random.random()

#     if sayi>0.5:
#         return "Tura"
#     else:
#         return "Yazı"

# print(yaziTuraAt())

# 3- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if (sayi>1):
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# asalSayilariBul(10,20)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i ==0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(15))
print(tamBolenleriBul(35))