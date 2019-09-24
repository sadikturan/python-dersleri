"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""
musteriAdi = 'Ali'
musteriSoyad = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
print(musteriAdSoyad)
musteriCinsiyet = True # Erkek
musteriTcKimlik = '13165465445'
musteriDogumYili = 1989
musteriAdresi = 'İstanbul Kadıköy'
musteriYasi = 2019 - musteriDogumYili 

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total:", total)