import ttkbootstrap as tb
from ttkbootstrap.constants import *

window = tb.Window(themename="darkly")

window.title("TTK Bootstrap")
window.geometry("500x700")

btn = tb.Button(window, text="Button", bootstyle="warning")
btn.pack(padx=20, pady=20)

window.mainloop()