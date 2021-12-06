sayilar = [1,5,8,9,3,45,77,5]
harfler = ['a','b','e','s','a','y']

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

# ekleme
sayilar.append(10)
sayilar.insert(3,5)
sayilar.insert(-1,50)
sayilar.insert(len(sayilar),150)

# silme
sayilar.pop()
sayilar.pop(0)
sayilar.remove(45)
harfler.remove('y')

# sıralama
sayilar.sort()
harfler.sort()
sayilar.reverse()

# print(sayilar.count(5))
# print(harfler.count('a'))

print(sayilar.index(3))
sayilar.clear()

sonuc = sayilar
# sonuc = harfler

print(sonuc)