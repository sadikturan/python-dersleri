import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
result = np.arange(5,15)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result = np.arange(50,100,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
result = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
result = np.random.randn(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
# result = np.random.randint(10,50,15).reshape(3,5)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
matris = np.random.randint(-50,50,15).reshape(3,5)
print(matris)
# rowTotal = matris.sum(axis = 1)
# colTotal = matris.sum(axis = 0)
# print(matris)
# print(rowTotal)
# print(colTotal)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
result = matris.max()
result = matris.min()
result = matris.mean()

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
result = matris.argmax()
result = matris.argmin()

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr = np.arange(10,20)
print(arr)

result = arr[:3]

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
result = arr[::-1]

# 15- Üretilen matrisin ilk satırını seçiniz.
result = matris[0]

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
result = matris[1,2]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result = matris[:,0]

# 18- Üretilen matrisin her bir elemanının karesini alınız.
result = matris ** 2

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
#     Aralığı (-50,+50) arasında yapınız.

ciftler = matris[matris % 2 == 0]
result = ciftler[ciftler>0]

print(result)