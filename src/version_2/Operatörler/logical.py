# yaş >= 18 ve (mezuniyet == 'lise' ya da  mezuniyet == 'üniversite')

x = -8

# 1- And Operatörü (ve)
# sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15) 

# True ve True => True
# False ve True => False
# False ve False => False

hak = 1
devam = 'e'

sonuc = (hak > 0) and (devam == 'e')

# or operatörü (veya)

sonuc = (x > 0) or (x % 2 == 0)

# True veya True => True
# False veya True => True
# False ve False => False

# not operatörü
sonuc = not(x > 0)


# x, 5-10 arasında bir çift sayı mı?

sonuc = ((x>5) and (x<10)) and (x%2==0)

print(sonuc)