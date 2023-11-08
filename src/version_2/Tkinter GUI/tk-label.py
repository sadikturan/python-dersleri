from tkinter import *

window = Tk()
window.geometry('500x500')

lbl1 = Label(window, 
            text='Label 1',
            # bg='red',
            fg='white', 
            # width=10, 
            # height=5,
            font=('Arial', 30),
            anchor='nw',
            padx=20, pady=30)

# lbl1['bg'] = 'blue'

# set value
lblValue = StringVar()
lbl1["textvariable"] = lblValue
lblValue.set('deneme')

# get value
print(lblValue.get())

# images
image = PhotoImage(file='logo.png')
lbl1['image'] = image

lbl1.pack()

window.mainloop()