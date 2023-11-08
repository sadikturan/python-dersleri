from datetime import date
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, "tr_TR")

window = tb.Window(themename="darkly")

window.title("DateEntry")
window.geometry("500x500")

def getDate():
    lbl.config(text=my_date.entry.get())

my_date = tb.DateEntry(window, bootstyle="warning", firstweekday=0, startdate=date(2022,5,9))
my_date.pack(pady=20)

lbl = tb.Label(window, text="", bootstyle="danger")
lbl.pack(pady=20)

btn = tb.Button(window, text="Get Date", bootstyle="success", command=getDate)
btn.pack(pady=20)


window.mainloop()