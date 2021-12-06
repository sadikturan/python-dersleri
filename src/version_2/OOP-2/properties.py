class Product:
    def __init__(self,name,price,description):
        self.name = name
        self.description = description
        if price >=0:
            self._price = price
        else:
            raise ValueError("fiyat için negatif değer ataması yapılmaz")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("fiyat için negatif değer ataması yapılmaz")

    @property
    def short_description(self):
        return self.description[:10]

    # def set_price(self,value):
    #     if value >=0:
    #         self._price = value
    #     else:
    #         raise ValueError("fiyat için negatif değer ataması yapılmaz")

    # def get_price(self):
    #     return self._price

p = Product("iphone 12", 9000,"iphone 12 apple in çıkardığı en yeni üründür ancak fiyatı çok pahalı.")

print(p.short_description)


