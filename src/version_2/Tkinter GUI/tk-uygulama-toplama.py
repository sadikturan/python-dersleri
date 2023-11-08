from tkinter import *

window = Tk()

def Topla():
    toplam = int(sayi1.get()) + int(sayi2.get())
    lblSonuc['text'] = toplam

Label(window, text='Sayı 1').grid(row=0,column=0, padx=20, pady=10)
Label(window, text='Sayı 2').grid(row=1,column=0)

sayi1 = Entry(window)
sayi2 = Entry(window)

sayi1.grid(row=0,column=1,padx=20)
sayi2.grid(row=1,column=1)

Button(window, text='Topla', command=Topla).grid(row=2,column=1,sticky='w',padx=20)

lblSonuc = Label(window)
lblSonuc.grid(row=3,column=1,sticky='w',padx=20)

window.mainloop()