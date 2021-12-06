# error handling => hata yönetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz', ex)
    else:
        break
    finally:
        print('try except sonlandı.')