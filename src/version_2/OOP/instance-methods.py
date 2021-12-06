class Person:

    # yapıcı metotlar (constructor)
    def __init__(self,name,surname,year):
        
        # object attributes, instance attributes
        self.name = name
        self.surname = surname
        self.year = year

    # instance methods
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}"

    def calculate_age(self):
        return f"{2021-self.year}"

# Object, Instance
p1 = Person("Sadık","Turan",1983)
p2 = Person("Sena","Turan",1999)

print(p1.intro())
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())