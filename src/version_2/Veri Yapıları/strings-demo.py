website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
sonuc = len(website)
sonuc = len(kursAdi)

# 2- 'website' içinden www karakterlerini alın.
sonuc = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
sonuc = kursAdi[0:15]
sonuc = kursAdi[:15]
sonuc = kursAdi[-15:]

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
sonuc = kursAdi[::-1]



# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print('abc ' * 3)

name, surname, age, job = 'Sadık','Turan', 37, 'öğretmen' 

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.' 

sonuc = "Benim adım " + name + " " + surname + ",Yaşım " + str(age) + " ve mesleğim " + job + "."
sonuc = "Benim adım {0} {1},Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
sonuc = f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}."

print(sonuc)
