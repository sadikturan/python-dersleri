# isim = "Sadık Turan"

# for harf in isim:
#     if (harf == "k"):
#         break
#     print(harf)

# i = 0
# while (i < 5):
#     i += 1
#     if (i == 3):
#         continue
#     print(i)

# print('döngü bitti.')

# 1-100 arasındaki çift sayılar toplamı.

i = 0
toplam = 0

while (i <= 100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam += i

print(f"toplam: {toplam}")

print("\U0001f600")