# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,'Merhaba')

# print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))

# asalSayılariBul(sayi1, sayi2)



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    
    return tamBolenler


print(tamBolenleriBul(20))