from tkinter import *

window = Tk()

window.geometry('500x500')


lbl1 = Label(window, text='Label 1')
lbl2 = Label(window, text='Label 2')
lbl3 = Label(window, text='Label 3')

# konumlandırma => pack, grid, place

# pack
# lbl1.pack()
# lbl2.pack(side='right')
# lbl3.pack(side='bottom')

# grid
# lbl1.grid(column=0,row=0)
# lbl2.grid(column=0,row=1)
# lbl3.grid(column=0,row=2)

# place
# lbl1.place(x=20,y=20)
# lbl2.place(x=20,y=50)
# lbl3.place(x=20,y=80)

lbl1.place(x=20,y=20)
lbl2.place(x=100,y=20)
lbl3.place(x=180,y=20)

window.mainloop()