from tkinter import *

window = Tk()
window.geometry('500x500')

frame1 = Frame(window, width=200, bg='red')
frame1.pack(fill=BOTH, side=LEFT, expand=True)

frame2 = Frame(window,width=200, bg='green')
frame2.pack(fill=BOTH, side=LEFT, expand=True)

frame3 = Frame(window,width=200, bg='blue')
frame3.pack(fill=BOTH, side=LEFT, expand=True)


window.mainloop()