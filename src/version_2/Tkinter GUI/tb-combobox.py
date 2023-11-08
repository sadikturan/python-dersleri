import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window = tb.Window(themename="darkly")

window.title("TTK Bootstrap")
window.geometry("500x700")

def bind_sehirler(e):
    lbl1.config(text='seçilen şehir:' + cb1.get())

def click_sehirler():
    lbl1.config(text='seçilen şehir:' + cb1.get())

sehirler = ['Kocaeli','Hatay','Rize','İstanbul']

lbl1 = tb.Label(text="Combobox",bootstyle="primary inverse", padding=20)
lbl1.pack(pady=10)

cb1 = tb.Combobox(values=sehirler, bootstyle='primary')
cb1.current(0)
cb1.pack(pady=10)

btn = tb.Button(text='Şehir Seçiniz', bootstyle='primary', command=click_sehirler)
btn.pack(pady=10)

cb1.bind('<<ComboboxSelected>>', bind_sehirler)

window.mainloop()