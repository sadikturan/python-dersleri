# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

benzinFiyat = 6.69
dizelFiyat = 5.86
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakıt tüketimi: '))
gidilecekYol = float(input('gidilecek yol kaç km: '))
yakitTipi = input('yakıt tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else:
    print('yanlış yakıt tipi girdiniz.')

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)