def dosya_kopyala(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(icerik)

# dosya_kopyala("msg.txt","msg_yeni.txt")

# dosya_kopyala fonksiyonunu işlevsel hale getiriniz.

def tert_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(icerik[::-1])

# tert_cevir("msg.txt","msg_ters.txt")

# eski dosyadaki tüm içerikleri yeni dosyaya tersten yazdırınız.

def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()

    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi": sum(len(satir) for satir in satirlar)
    }
    return sonuc

print(bilgilendir("msg.txt"))
print(bilgilendir("newfile.txt"))

# fonksiyona gönderilen dosya içindeki verilerin özet bilgisini hazırlayınız.
# {'satir_sayisi': 52, 'kelime_sayisi': 158, 'karakter_sayisi': 1250}