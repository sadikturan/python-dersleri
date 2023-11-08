import ttkbootstrap as tb
from ttkbootstrap.constants import *

window = tb.Window(themename="darkly")

window.title("TTK Bootstrap")
window.geometry("500x600")

i = 0
def changeColor():
    global i
    if(i == 0):
        lbl1.config(bootstyle="danger inverse")
        i = 1
    else:
        lbl1.config(bootstyle="white inverse")
        i = 0

frm = tb.Frame(window)
frm.pack(padx=10,pady=(20,0), fill=X)

lbl1 = tb.Label(frm, text="Label", bootstyle="white inverse", padding=20, anchor=CENTER)
lbl1.pack(pady=(0,20), fill=X)

lbl2 = tb.Label(frm, text="Label", bootstyle="danger inverse", padding=20, anchor=CENTER)
lbl2.pack(fill=X)

btn1 = tb.Button(frm, text="Button", bootstyle="light outline", padding=20, command=changeColor)
btn1.pack(fill=X, pady=(20,0))

window.mainloop()