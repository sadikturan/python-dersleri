names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
# names.append('Cenk')

# 2-  "Sena" değerini listenin başına ekleyiniz.
# names.insert(0, 'Sena')
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')

# 3-  "Deniz" ismini listeden siliniz.
# names.remove('Deniz')
# names.pop()
# names.pop(1)

# 4-  "Deniz" isminin indeksi nedir ?
# index  = names.index('Deniz')
# names.pop(index)

# 5-  "Ali" listenin bir elemanı mıdır ?
# result = 'Ali' in names
# result = names.index('Ali')

# 6-  Liste elemanlarını ters çevirin.
# names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# names.sort()

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# str = "Chevrolet,Dacia"
# result = str.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# min = min(years)
# max = max(years)
# print(min, max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
# result = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.
# years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)