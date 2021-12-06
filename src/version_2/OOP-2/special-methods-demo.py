class NewDict(dict):
    def __repr__(self):
        print('repr metondundan mesaj var.')
        return super().__repr__()

    def __missing__(self,key):
        print("olmayan key bilgisi istiyorsunuz.")

    def __getitem__(self,key):
        print("bir elemanı çağırıyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self,key,value):
        print("listeye eleman ekliyorsunuz.")
        super().__setitem__(key,value)

    def __contains__(self,item):
        print("listede eleman arayamasınız")
        return super().__contains__(item)

data = NewDict({"first":"Sadık","last":"Turan"})


print(data["first"])
data["age"]
data["first"]="Çınar"

print(data)

print("first" in data)