# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur. 
with open("/users/sadikturan/documents/newfile.txt","w",encoding="UTF-8") as file:
    file.write("Çınar Turan\n")
    file.write("Sadık Turan\n")
    file.write("Sena Turan")
    print(file)

with open("/users/sadikturan/documents/newfile.txt") as file:
    print(file.read())