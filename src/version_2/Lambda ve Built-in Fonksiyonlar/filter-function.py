yaslar = [5,12,18,24,45]

def yetiskinmi(x):
    if x<18:
        return False
    else: 
        return True

sonuc = list(filter(yetiskinmi, yaslar))
sonuc = list(filter(lambda x: x>=18, yaslar))

sayilar = [0,1,25,6,8,9]
sonuc = list(filter(lambda x: x%2!=0, sayilar))

isimler = ["çınar","yiğit","sena","ada","ali"]
sonuc = list(filter(lambda n: n[0]=='a',isimler))

filteredResult = filter(lambda n: n[0]=='a',isimler)
sonuc = list(map(lambda n: n.upper(), filteredResult))

users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"]},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": ["tweet 1"]}
]

sonuc = list(filter(lambda u: len(u["tweets"])>0, users))
sonuc = list(map(lambda  u: u["username"].upper(), filter(lambda u: len(u["tweets"])>0, users)))

sonuc = [user["username"].upper() for user in users if len(user["tweets"])>0]

print(sonuc)