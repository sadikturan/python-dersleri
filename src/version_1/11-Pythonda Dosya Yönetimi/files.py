# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 

# file = open("newfile.txt","w")
# file = open("C:/users/sadikturan/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Sadık Turan")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nÇınar Turan")
# file.write("Çınar Turan\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
