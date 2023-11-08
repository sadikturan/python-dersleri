from tkinter import *

window = Tk()
window.geometry('500x500')


Button(window, text='Tıkla').pack()
Button(window, text='Tıkla', padx=10).pack()
Button(window, text='Tıkla', padx=30).pack()
Button(window, text='Tıkla', padx=30, pady=30, state='disabled').pack()

def btnClick():
    lblSonuc['text'] += input.get() + ' '
    input.delete(0, 'end')

input = Entry(window)
lblSonuc = Label(window)
Button(window, text='Göster', command= btnClick).pack()
Button(window, text='Çıkış', command= window.quit).pack()

input.pack()
lblSonuc.pack()

window.mainloop()