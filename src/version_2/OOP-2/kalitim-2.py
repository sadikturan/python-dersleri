class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass

p1 = Person("Ahmet","Turan",20)
p1.intro()

s1 = Student("Ali","Yılmaz",25)
s1.intro()

t1 = Teacher("Can","Yılmaz",25)
t1.intro()