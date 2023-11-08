from tkinter import *


window = Tk()
window.geometry("280x130")
window.title("Grid Layout")
window.resizable(width=False, height=False)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = Label(window, text='Username')
username_label.grid(column=0, row=0, sticky='w', padx=5,pady=5)

username_entry = Entry(window)
username_entry.grid(column=1, row=0, sticky='e', padx=5, pady=5)

password_label = Label(window, text='Password')
password_label.grid(column=0, row=1, sticky='w', padx=5,pady=5)

password_entry = Entry(window)
password_entry.grid(column=1, row=1, sticky='e', padx=5, pady=5)

login_button = Button(window, text='Login')
login_button.grid(column=1, row=2, sticky='e', padx=5, pady=5)

window.mainloop()