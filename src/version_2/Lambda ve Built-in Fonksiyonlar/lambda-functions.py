# sonuc = (lambda a: a ** 2)(3)
multiply = lambda a: a ** 2
sonuc = multiply(5)

toplama = lambda a,b,c: a+b+c
sonuc = toplama(1,4,7)

tersCevir = lambda s: s[::-1]
sonuc = tersCevir("Sadık")

def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(3)

sonuc = multiply2(10)
sonuc = multiply2(20)
sonuc = multiply3(10)


print(sonuc)