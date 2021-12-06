# Deste sınıfı

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"

class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]
        print(self.kartlar)

deste1 = Deste()
deste2 = Deste()


