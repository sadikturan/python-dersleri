
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi = float(input('sayı: '))
# result = (sayi > 0) and (sayi<=100)
# print(f'sayı 0-100 arasındamı: {result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi = int(input('sayı: '))
# result = (sayi > 0) and (sayi % 2 ==0)
# print(f'girilen sayı pozitif çift sayı mı: {result}')


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# result = (girilenEmail == email) and (girilenPassword == password)
# print(f'uygulamaya giriş başarılı mı: {result}')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and  (a > c)
# print(f'a en büyük sayıdır : {result}')

# result = (b > a) and (b > c)
# print(f'b en büyük sayıdır : {result}')

# result = (c > a) and (c > b)
# print(f'c en büyük sayıdır : {result}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final : '))

# ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
# result = (ortalama>=50) and (final>=50)
# result = (ortalama >=50) or (final>=70)

# print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')




# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')


