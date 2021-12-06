# 1- Girilen 2 sayıdan hangisi büyüktür ?
# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))

# sonuc = (sayi1 > sayi2) # True, False
# print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")

# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sayi = int(input('sayı: '))

# sonuc = (sayi % 2 == 0)
# print(f"{sayi} çift sayıdır: {sonuc}")

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
# sayi = int(input("sayı: "))
# sonuc = (sayi > 0) # Pozitif
# print(f"girilen sayı pozitif: {sonuc}")

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1 = float(input("vize 1: "))
# vize2 = float(input("vize 2: "))
# final = float(input("final: "))

# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
# print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: info@sadikturan.com parola:12345)

_email = "info@sadikturan.com"
_password = "12345"

email = input("email: ")
password = input('password: ')

isEmail = (email.lower().strip() == _email)
isPassword = (password.strip() == _password)

print(f"email doğruluğu: {isEmail} ve parola doğruluğu: {isPassword}")