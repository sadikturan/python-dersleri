sayilar = [1,53,45,67,97,5,7]

# sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,53,45,67,97,5,7))


users = [
    {"username":"sadikturan", "tweets":["tweet 1","tweet 2"],"email":"info@gmail.com"},
    {"username":"cinarturan", "tweets":[]},
    {"username":"senaturan", "tweets":["tweet 1"],"name":"","phone":"434312134"}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda  user: len(user["tweets"]))

kurslar = [
    {"title":"python kursu","students":25000},
    {"title":"web geliştirme kursu","students":35000},
    {"title":"javascript kursu","students":5000}
]

sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True)
sonuc = map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True))

print(list(sonuc))