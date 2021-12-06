liste = [1,2,3]
print(len(liste))

s = "hello world"
print(len(s))

class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure

    def __str__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi."

    def __repr__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi."

    def __len__(self):
        return self.sure

    def __del__(self):
        print("film objesi silindi.")

f = Film("film adı","yonetmen",120)

print(str(liste))
print(str(f))
print(len(f))



