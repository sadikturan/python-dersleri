from tkinter import *

window = Tk()
window.geometry('500x500')

input = Entry(window, 
    width=15, 
    #show="*"
    font=('Arial 16'),
)

lbl1 = Label(window)
lbl1.pack()

inputValue = StringVar()
input['textvariable'] = inputValue
inputValue.set('deneme deneme deneme deneme')

# methods
input.insert(0, 'abc')
# input.delete(0, 2)
input.delete(0, 'end')

print(input.get())
lbl1['text'] = input.get()
print(inputValue.get())

input.pack()


window.mainloop()