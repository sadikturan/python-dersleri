from tkinter import *
import math

class Calculator:
    def action(self,arg):
        self.e.insert(END, arg)

    def equals(self):
        try:
            self.value = eval(self.e.get())
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'hatalı bilgi')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def clear(self):
        self.e.delete(0, END)

    def square(self):
        try:
            self.value = eval(self.e.get())
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'hatalı bilgi')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def __init__(self, window):
        window.title("Hesap Makinesi")
        window.resizable(width=False,height=False)

        self.e = Entry(window, font=('Arial', 22), relief='sunken')
        self.e.pack(fill=X, pady=8, padx=5)
        self.e.focus_set()

        self.frame = Frame(window, pady=5, padx=5)
        self.frame.pack()

        Button(self.frame, text="7", width=5, height=3,command=lambda:self.action('7')).grid(row=0,column=0)
        Button(self.frame, text="8", width=5, height=3,command=lambda:self.action('8')).grid(row=0,column=1)
        Button(self.frame, text="9", width=5, height=3,command=lambda:self.action('9')).grid(row=0,column=2)
        Button(self.frame, text="/", width=5, height=3,command=lambda:self.action('/')).grid(row=0,column=3)
        Button(self.frame, text="AC", width=5, height=3,command=lambda:self.clear()).grid(row=0,column=4)

        Button(self.frame, text="4", width=5, height=3,command=lambda:self.action('4')).grid(row=1,column=0)
        Button(self.frame, text="5", width=5, height=3,command=lambda:self.action('5')).grid(row=1,column=1)
        Button(self.frame, text="6", width=5, height=3,command=lambda:self.action('6')).grid(row=1,column=2)
        Button(self.frame, text="*", width=5, height=3,command=lambda:self.action('*')).grid(row=1,column=3)
        Button(self.frame, text="x²", width=5, height=3,command=lambda:self.square()).grid(row=1,column=4)

        Button(self.frame, text="1", width=5, height=3,command=lambda:self.action('1')).grid(row=2,column=0)
        Button(self.frame, text="2", width=5, height=3,command=lambda:self.action('2')).grid(row=2,column=1)
        Button(self.frame, text="3", width=5, height=3,command=lambda:self.action('3')).grid(row=2,column=2)
        Button(self.frame, text="-", width=5, height=3,command=lambda:self.action('-')).grid(row=2,column=3)

        Button(self.frame, text="0", width=5, height=3,command=lambda:self.action('0')).grid(row=3,column=0)
        Button(self.frame, text=".", width=5, height=3,command=lambda:self.action('.')).grid(row=3,column=1)
        Button(self.frame, text="%", width=5, height=3,command=lambda:self.action('%')).grid(row=3,column=2)
        Button(self.frame, text="+", width=5, height=3,command=lambda:self.action('+')).grid(row=3,column=3)

        Button(self.frame, text="=", width=5, height=7,command=lambda:self.equals()).grid(row=2,column=4,rowspan=2)


window = Tk()
Calculator(window)
window.mainloop()
        