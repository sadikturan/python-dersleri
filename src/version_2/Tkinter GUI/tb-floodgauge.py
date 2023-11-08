import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window = tb.Window(themename="darkly")

window.title("TTK Bootstrap")
window.geometry("500x700")

my_gauge = tb.Floodgauge(window, bootstyle="primary", font=("Arial", 18), value=10, mask="{}%", max=80)
my_gauge.pack(fill=X, padx=20, pady=20)


window.mainloop()