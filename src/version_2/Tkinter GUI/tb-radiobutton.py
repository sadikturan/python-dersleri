import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window = tb.Window(themename="cosmo")

window.title("TTK Bootstrap")
window.geometry("500x700")

# liste = ["YüksekLisans","Lisans","Lise","Ortaokul","İlkokul"]
liste = {
    "YüksekLisans":"1",
    "Lisans":"2",
    "Lise":"3",
    "Ortaokul":"4",
    "İlkokul":"5"
}

def get_value():
    lbl.config(text=egitim_var.get())

egitim_var = StringVar()

for (text,value) in liste.items():
    tb.Radiobutton(window, bootstyle="primary", value=value, text=text, variable=egitim_var, command=get_value).pack(pady=10)

# rb1 = tb.Radiobutton(window, bootstyle="primary", value="1", text="Lisans", variable=egitim_var, command=get_value)
# rb1.pack(pady=20)

# rb1 = tb.Radiobutton(window, bootstyle="primary", value="2", text="Lise", variable=egitim_var, command=get_value)
# rb1.pack(pady=20)

lbl = tb.Label(window, text="", bootstyle="warning")
lbl.pack(pady=20)

btn = tb.Button(window, text="Get Value", bootstyle="primary", command=get_value)
btn.pack(pady=20)


window.mainloop()