msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan"

# sonuc = msg.upper()
# sonuc = msg.lower()
# sonuc = msg.title()
# sonuc = msg.capitalize()

# sonuc = "abc".islower()

# sonuc = "    abc ".strip()
# sonuc = msg.split()
# sonuc = msg.split('.')

# sonuc = "-".join(sonuc)

# index = msg.index('Hoş')
# sonuc = msg.startswith('A')
# sonuc = msg.endswith('n')

sonuc = msg.replace('Sadık','Çınar')
sonuc = msg.lower().replace(' ','-').replace('ş','s').replace('.','').replace('ı','i')


print(sonuc)