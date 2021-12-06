def toplam():
    return 10+20

sonuc = toplam() + 50

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 1983

sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour


def selamla():
    if (saat()<12):
        return "Günaydın"
    else:
        return "Merhaba"

sonuc = selamla() + ",Sadık"

print(sonuc)