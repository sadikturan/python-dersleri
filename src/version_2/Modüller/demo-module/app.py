"""
    module1 (db)      : urunler
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)     :

        yeni ürün ekleme => urunEkle("iphone 11 pro", 7000)
        ürün güncelle    => urunGuncelle(1, "iphone 12 pro", 8000)
        ürünleri listele => urunleriGetir() 
"""


from methods import *

urunleriGetir()
print("******")

urunEkle("iphone 11 pro", 8000)
urunEkle("iphone 7s", 5000)

urunGuncelle(6, "iphone 8s", 6000)
print('******')
urunleriGetir()



