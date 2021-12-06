ad = 'Sadık'
soyad = 'Turan'
yas = '37'

msj = 'Benim adım ' + ad + ' ve soyadım ' + soyad + '.Yaşım ise ' + yas + '.'
karakterSayisi = len(msj)

print(msj[0])                   # B
print(msj[1])                   # e
print(msj[-1])                  # .
print(msj[karakterSayisi - 1])  # .

print(msj[0:5])
print(msj[6:16])
print(msj[:10])
print(msj[10:])

print(msj[-10:-1])
print(msj[0:40:2])
print(msj[::1])
print(msj[::-1])
