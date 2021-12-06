class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name,surname,age)
        self.number = number
        print("student nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalıyor.")

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name,surname,age)
        self.branch = branch
        print("teacher nesnesi türetildi.")
    
    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimi veriyor.")

p1 = Person("Ahmet","Turan",20)
p1.intro() # person

s1 = Student("Ali","Yılmaz",25, 101)
s1.intro() # student
s1.study()

t1 = Teacher("Can","Yılmaz",25, "ingilizce")
t1.intro()
t1.teach()