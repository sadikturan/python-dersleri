from tkinter.messagebox import showinfo
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *
import time

window = tb.Window(themename="superhero")

window.title("TTK Bootstrap")
window.geometry("500x500")

def increment():
    if(my_progressbar["value"] < 100):
        my_progressbar["value"] += 20
        my_label.config(text=my_progressbar["value"])
    else:
        showinfo(message="bitti")

def start():
    my_progressbar.start()

def stop():
    my_progressbar.stop()

def auto():
    for i in range(10):
        my_progressbar["value"] += 10
        my_label.config(text=my_progressbar["value"])
        window.update()
        time.sleep(0.5)

my_progressbar = tb.Progressbar(window, 
                                orient="horizontal", 
                                bootstyle="primary striped",
                                maximum=100,
                                value=0)

my_progressbar.pack(pady=20, padx=20, fill=X)

my_label = tb.Label(window, text="", font=("Arial", 18))
my_label.pack()

my_frame = tb.Frame(window)
my_frame.pack(pady=40)

btn_1 = tb.Button(my_frame, text="++", bootstyle="primary", command=increment)
btn_1.grid(column=0, row=0, padx=20)

btn_2 = tb.Button(my_frame, text="start", bootstyle="primary", command=start)
btn_2.grid(column=1, row=0, padx=20)

btn_3 = tb.Button(my_frame, text="stop", bootstyle="primary", command=stop)
btn_3.grid(column=2, row=0, padx=20)

btn_4 = tb.Button(my_frame, text="auto", bootstyle="primary", command=auto)
btn_4.grid(column=3, row=0, padx=20)

my_label.config(text=my_progressbar["value"])

window.mainloop()