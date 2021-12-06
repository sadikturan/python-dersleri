diller = ["Python","C#","Java","Javascript","React"]

sonuc = diller
sonuc = type(diller)
sonuc = diller[0:2]
sonuc = diller[2:]
sonuc = diller[:3]
sonuc = diller[-1]
sonuc = diller[-4:-1]
# diller[0] = "Html"
diller[-1] = "Html"
sonuc = len(diller)
sonuc = diller + ["Angular","Vuejs"]

# if bloğu=> Koşul ifadeleri
if "Python" in diller:
    print("değer listenin bir elemanı")

# döngüler
for x in diller:
    print(x)

del diller[0]

sonuc = diller

print(sonuc)