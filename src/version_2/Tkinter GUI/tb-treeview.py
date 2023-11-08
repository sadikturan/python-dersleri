import ttkbootstrap as tb
from tkinter import *
import sqlite3

window = tb.Window(themename="cosmo")
window.title("Treeview")
window.geometry("850x700")

def get_ogrenciler():
    connection = sqlite3.connect("okul.db")
    cursor = connection.cursor()
    cursor.execute("select * from ogrenciler")
    ogrenciler = cursor.fetchall()
    connection.close()
    return ogrenciler

def addStudent():
    ad = txt_firstName.get()
    soyad = txt_lastName.get()
    email = txt_email.get()

    connection = sqlite3.connect("okul.db")
    cursor = connection.cursor()
    sql = "INSERT INTO ogrenciler(Ad, Soyad,Email) VALUES (?,?,?)"
    values = (ad, soyad, email)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()

    # id = len(tvw.get_children()) + 1
    id= cursor.lastrowid
    tvw.insert("", END, values=(id, ad, soyad, email))
    
    txt_firstName.delete(0, END)
    txt_lastName.delete(0, END)
    txt_email.delete(0, END)

def remove_one():
    selected_item = tvw.focus()
    delete_id = tvw.item(selected_item)["values"][0]

    connection = sqlite3.connect("okul.db")
    cursor = connection.cursor()
    sql = "DELETE FROM ogrenciler WHERE id=" + str(delete_id)
    cursor.execute(sql)
    connection.commit()
    connection.close()

    # delete from db
    # delete from treeview
    tvw.delete(selected_item)

def remove_all():
    items = tvw.get_children()
    for item in items:
        tvw.delete(item)

    connection = sqlite3.connect("okul.db")
    cursor = connection.cursor()
    sql = "DELETE FROM ogrenciler"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def selectItem(e):
    selected_item = tvw.focus()
    ogrenci = tvw.item(selected_item)["values"]

    txt_firstName.delete(0, END)
    txt_lastName.delete(0, END)
    txt_email.delete(0, END)

    txt_firstName.insert(0, ogrenci[1])
    txt_lastName.insert(0, ogrenci[2])
    txt_email.insert(0, ogrenci[3])

def updateStudent():
    selected_item = tvw.focus()
    id = tvw.item(selected_item)["values"][0]

    ad = txt_firstName.get()
    soyad = txt_lastName.get()
    email = txt_email.get()

    tvw.item(selected_item, text="", values=(id, ad, soyad, email))

    connection = sqlite3.connect("okul.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE ogrenciler SET Ad = :ad, Soyad = :soyad, Email = :email WHERE id = :id", {
        "id" : id,
        "ad" : ad,
        "soyad" : soyad,
        "email" : email
    })
    connection.commit()
    connection.close()


my_frame = tb.Frame(window)
my_frame.pack(pady=10, padx=10)

my_scroll = Scrollbar(my_frame, orient="vertical")
my_scroll.pack(side="right", fill="y")

tvw = tb.Treeview(my_frame, show="headings", height=20, bootstyle="secondary", yscrollcommand=my_scroll.set)
tvw.pack()

tvw.bind("<ButtonRelease-1>", selectItem)

my_scroll.config(command=tvw.yview)

# column
tvw["column"] = ("id","firstname","lastname","email")

tvw.column("#0", width=50, minwidth=30)
tvw.column("#1", width=200, minwidth=100)
tvw.column("#2", width=200, minwidth=100)
tvw.column("#2", width=200, minwidth=100)

# heading
tvw.heading("id", text="Id", anchor="w")
tvw.heading("firstname", text="Ad", anchor="w")
tvw.heading("lastname", text="Soyad", anchor="w")
tvw.heading("email", text="Eposta", anchor="w")

for ogrenci in get_ogrenciler():
    tvw.insert("", END, values=(ogrenci[0],ogrenci[1],ogrenci[2],ogrenci[3]))

# add frame
add_frame = tb.LabelFrame(window, bootstyle="secondary",padding=15, text="Yeni Kayıt")
add_frame.pack(pady=10, padx=(15,20), fill=X)

lbl_firstName = tb.Label(add_frame, text="Ad",width=10)
lbl_firstName.grid(row=0, column=0,pady=5,sticky="w")

lbl_lastName = tb.Label(add_frame, text="Soyad")
lbl_lastName.grid(row=1, column=0,pady=5,sticky="w")

lbl_email = tb.Label(add_frame, text="Email")
lbl_email.grid(row=2, column=0,pady=5,sticky="w")

txt_firstName = tb.Entry(add_frame, width=75)
txt_firstName.grid(row=0, column=1,pady=5)

txt_lastName = tb.Entry(add_frame, width=75)
txt_lastName.grid(row=1, column=1,pady=5)

txt_email = tb.Entry(add_frame, width=75)
txt_email.grid(row=2, column=1,pady=5)

# update buton
add_update_frame = Frame(add_frame)
add_update_frame.grid(row=3, column=1,sticky="w")

btn_add = tb.Button(add_update_frame, text="Kaydet", bootstyle="secondary outline", command=addStudent)
btn_add.pack(side=LEFT)

btn_update = tb.Button(add_update_frame, text="Güncelle", bootstyle="secondary outline", command=updateStudent)
btn_update.pack(side=LEFT, padx=5)

# remove butonları
btn_frame = tb.LabelFrame(window, bootstyle="secondary", padding=15, text="Delete Buttons")
btn_frame.pack(pady=10, padx=(15,20), fill=X)

btn_remove_one = tb.Button(btn_frame, text="Sil", bootstyle="secondary outline", command=remove_one)
btn_remove_one.pack(side="right", padx=10)

btn_remove_all = tb.Button(btn_frame, text="Hepsini Sil", bootstyle="secondary outline", command=remove_all)
btn_remove_all.pack(side="right", padx=10)

window.mainloop()