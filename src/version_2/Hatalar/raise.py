# print(10 / 0)

# x = 10

# if x > 5:
#     raise ValueError('x 5 den büyük olamaz.')

def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır.")

    if type(color) is not str:
        raise TypeError("renk str tipinde olmalıdır.")

    if color not in colors:
        raise ValueError("geçersiz bir renk ismi.")

    print(f"{text} {color} olarak yazdırıldı.")

# try:
#     colorize("selam","yellow")
# except Exception as ex:
#     print(ex)

try:
    colorize("selam","red")
    colorize("selam","yellow")
except (TypeError,ValueError) as ex:
    print(ex)