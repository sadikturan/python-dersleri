import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.ogrenci
sonuc = module.ogrenci["ad"]
sonuc = module.ogrenci["notlar"]
sonuc = module.topla(10,20)

import module as m

sonuc = m.sayilar

from module import ogrenci, topla

sonuc = ogrenci
sonuc = topla(10,20)

from module import *

sonuc = sayi
sonuc = ogrenci["notlar"]

print(sonuc)