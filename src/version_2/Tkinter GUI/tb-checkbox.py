import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window = tb.Window(themename="darkly")

window.title("TTK Bootstrap")
window.geometry("500x700")

def checkedValue():
    if ch1_var.get() == 1:
        lbl.config(text="Checked")
    else:
        lbl.config(text="UnChecked")

lbl = tb.Label(bootstyle="danger inverse", text='Not Selected', padding=20)
lbl.pack(pady=20)

ch1_var = IntVar(value=0)
ch1 = tb.Checkbutton(bootstyle='danger', text='Checked', variable=ch1_var, onvalue=1, offvalue=0, command=checkedValue)
ch1.pack(pady=10)

ch2 = tb.Checkbutton(bootstyle='danger toolbutton', text='Checked', variable=ch1_var)
ch2.pack(pady=10)

ch3 = tb.Checkbutton(bootstyle='warning toolbutton outline', text='Checked', variable=ch1_var)
ch3.pack(pady=10)

ch4 = tb.Checkbutton(bootstyle='secondary round-toggle', text='Checked', variable=ch1_var)
ch4.pack(pady=10)

ch5 = tb.Checkbutton(bootstyle='success square-toggle', text='Checked', variable=ch1_var) 
ch5.pack(pady=10)

window.mainloop()