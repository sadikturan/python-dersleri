# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

# sayi = int(input('sayı: '))
# sonuc = (sayi > 50) and (sayi<=100)
# print(f"{sayi}, 50 ile 100 arasındadır: {sonuc}")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
# sayi = int(input('sayı: '))
# sonuc = (sayi > 0) and (sayi % 2 == 1)
# print('girilen sayı pozitif tek sayıdır: ', sonuc)

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
# _username = "sadikturan"
# _password = "1234"

# girilenUsername = input('username: ')
# girilenPassword = input('parola: ')

# sonuc = (girilenUsername == _username) and (girilenPassword == _password)
# print('girilen username ve parola doğru: ', sonuc)

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))

# sonuc = (x>y) and (x>z) # x en büyük
# print("x en büyük sayı: ", sonuc)

# sonuc = (y>x) and (y>z) # y en büyük
# print("y en büyük sayı: ", sonuc)

# sonuc = (z>x) and (z>y) # z en büyük
# print("z en büyük sayı: ", sonuc)

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final: '))

# ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
# # sonuc1 = ortalama>=50
# # sonuc = (ortalama >= 50) and (final>=50)
# sonuc = (ortalama >= 50) or (final>=70)

# print(f"öğrencini not ortalaması: {ortalama} ve geçme durumu: {sonuc}")

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

zayif = (kiloIndeks >= 0) and (kiloIndeks <=18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <=24.9)
kilolu = (kiloIndeks > 24.9) and (kiloIndeks <=29.9)
obez = (kiloIndeks >= 29.9) and (kiloIndeks <=34.9)

print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez: {obez}")
