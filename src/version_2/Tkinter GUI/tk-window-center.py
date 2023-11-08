from tkinter import *

window = Tk()

# title
window.title('pencere başlığı')

# zemin rengi
window.configure(bg='#495E57')

# pencerenin ortalanması
window_height = 500
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window.mainloop()