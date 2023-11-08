from tkinter import *

window = Tk()

window.title('pencere başlığı')
window.geometry('500x500')

def deleteItem():
    lb.delete(ANCHOR)

def selectItem():
    lbl.config(text=lb.get(ANCHOR))

lb = Listbox(window)
lb.pack(pady=20)

# add item to lb
lb.insert(0, "item 1")
lb.insert(1, "item 2")
lb.insert(END, "item 3")

# add list to lb
liste = ("one","two","three")

for item in liste:
    lb.insert(END, item)

btn1 = Button(window, text="Sil", command=deleteItem)
btn1.pack(pady=15)

btn2 = Button(window, text="Eleman Seç", command=selectItem)
btn2.pack(pady=15)

lbl = Label(window, text='')
lbl.pack(pady=15)

window.mainloop()