def selamlama(isim="Kullanıcı", mesaj="İyi Günler"):
    print(f"{mesaj} {isim}")

selamlama("Ali","Günaydın")
selamlama("Ali","İyi günler")
selamlama("Ali")
selamlama()

def usAlma(taban, us=3):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(2,3)
sonuc = usAlma(3)

def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def islem(a,b,fn = toplam):
    return fn(a,b)

sonuc = islem(5,3,cikarma)
sonuc = islem(5,5)

print(sonuc)