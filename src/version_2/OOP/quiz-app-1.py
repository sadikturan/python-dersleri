# Her bir soruyu temsil edecek question nesnesi oluşturunuz.

# Question sınıfı
#   - text    => soru
#   - choices => cevap şıkları
#   - answer  => soru

# checkAnswer() metodu ile cevap kontrolü yapınız.

# q1.checkAnswer('cevap') => True
# q1.checkAnswer('cevap') => False

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer == answer

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")

print(q1.text)
print(q1.choices)
print(q1.answer)

sonuc = q1.checkAnswer('java')
print(sonuc)





