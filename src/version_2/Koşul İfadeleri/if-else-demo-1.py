# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

# sayi = int(input('sayı: '))
# if  (sayi > 50) and (sayi<=100):
#     print(f"{sayi}, 50 ile 100 arasındadır.")
# else:
#     print(f"{sayi}, 50 ile 100 arasında değildir.")


# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

# sayi = int(input('sayı: '))
# if (sayi > 0):
#     if (sayi % 2 == 1):
#         print('girilen sayı pozitif tek sayıdır.')
#     else:
#         print('sayı pozitif ancak tek değil.')
# else:
#     print('girilen sayı negatif.')


# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
# _username = "sadikturan"
# _password = "1234"

# girilenUsername = input('username: ')
# girilenPassword = input('parola: ')

# if (girilenUsername.strip() == _username) and (girilenPassword.strip() == _password):
#     print('girilen username ve parola doğru')
# else:
#     print('girilen bilgiler yanlış')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))

# if (x>y) and (x>z):
#     print("x en büyük sayı: ")
# elif (y>x) and (y>z):
#     print("y en büyük sayı: ")
# elif (z>x) and (z>y):
#     print("z en büyük sayı: ")


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    c-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final: '))

# ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
# sonuc = ortalama>=50
# sonuc = (ortalama >= 50) and (final>=50)
# sonuc = (ortalama >= 50) or (final>=70)

# durum 1
# if(ortalama>=50):
#     print(f"öğrencini not ortalaması: {ortalama} ve sınıfı geçti")
# else:
#     print(f"öğrencini not ortalaması: {ortalama} ve kaldı.")

# durum 2
# if (ortalama>=50):
#     if(final>=50):
#         print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci geçti.')
#     else:
#         print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı. Finalden en az 50 almalıdır.')
# else:
#     print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı.')

# durum 3
# if(ortalama>=50):
#     print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci geçti.')
# else:
#     if (final>=70):
#         print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci başarılı çünkü finalden 70 üstü aldı.')
#     else:
#         print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı.')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)

if (kiloIndeks >= 0) and (kiloIndeks <=18.4):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf.")
elif (kiloIndeks > 18.4) and (kiloIndeks <=24.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal.")
elif (kiloIndeks > 24.9) and (kiloIndeks <=29.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu.")
elif (kiloIndeks >= 29.9) and (kiloIndeks <=34.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez.")
else:
    print('bilgileriniz yanlış.')
