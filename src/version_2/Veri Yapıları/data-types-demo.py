'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)

pi = 3.14

r = float(input("yarı çap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

result = "alan: " + str(alan) + " çevre: " + str(cevre)
print(result)

'''

'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''

print("kaç km yol gittiniz?")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)

print(str(mesafeKm) + " km = " + str(mesafeMil) + " mil.")
