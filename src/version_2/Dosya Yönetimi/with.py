try:
    with open("msg.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatası: ", e)
finally:
    print("dosya kapandı")
    

