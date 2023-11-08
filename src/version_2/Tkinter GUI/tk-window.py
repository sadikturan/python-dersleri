from tkinter import *

window = Tk()

# title
window.title('pencere başlığı')

# zemin rengi
window.configure(bg='#495E57')

# konum - boyut
window.geometry('500x500+200+200')

# resize
window.resizable(width=True, height=True)
# window.minsize(400,400)
# window.maxsize(700,700)

# fullscreen
# window.attributes('-fullscreen', 1)
# window.bind('<Escape>', lambda event: window.attributes('-fullscreen', 0))

window.mainloop()