import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # set window config
        self.geometry("600x350")
        self.title("Listbox")
        self.resizable(0,0)

        # set layouts
        self.create_layouts()

        # set widgets
        self.create_widgets()

    def create_layouts(self):
        main_frame = ttk.Frame(self, padding=50)
        main_frame.pack()

        self.frame1 = ttk.Frame(main_frame)
        self.frame1.grid(row=0, column=0)

        self.frame2 = ttk.Frame(main_frame)
        self.frame2.grid(row=0, column=1)

        self.frame3 = ttk.Frame(main_frame)
        self.frame3.grid(row=0, column=2)

        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=3)

    def create_widgets(self):
        # frame 1
        self.frame1_add_box = ttk.Frame(self.frame1)
        self.frame1_add_box.pack(pady=10)

        self.entry_add_1 = ttk.Entry(self.frame1_add_box, width=15)
        self.entry_add_1.pack(side=tk.LEFT)

        self.btn_add_1 = ttk.Button(self.frame1_add_box, text='+', width=2)
        self.btn_add_1.pack(side = tk.LEFT)

        self.listbox_1 = tk.Listbox(self.frame1)
        self.listbox_1.pack()

        self.frame1_delete_box = ttk.Frame(self.frame1)
        self.frame1_delete_box.pack(pady=10)

        self.btn_delete_1 = ttk.Button(self.frame1_delete_box, text='Sil')
        self.btn_delete_1.pack(side=tk.LEFT)

        self.btn_delete_all_1 = ttk.Button(self.frame1_delete_box, text='Hepsini Sil')
        self.btn_delete_all_1.pack(side=tk.LEFT)    

        # frame 2
        self.btn_right = ttk.Button(self.frame2, text='>')
        self.btn_right.pack()

        self.btn_left = ttk.Button(self.frame2, text='<')
        self.btn_left.pack()

        self.btn_right_all = ttk.Button(self.frame2, text='>>')
        self.btn_right_all.pack()

        self.btn_left_all = ttk.Button(self.frame2, text='<<')
        self.btn_left_all.pack()

        # frame 3
        self.frame3_add_box = ttk.Frame(self.frame3)
        self.frame3_add_box.pack(pady=10)

        self.entry_add_2 = ttk.Entry(self.frame3_add_box, width=15)
        self.entry_add_2.pack(side=tk.LEFT)

        self.btn_add_2 = ttk.Button(self.frame3_add_box, text='+', width=2)
        self.btn_add_2.pack(side = tk.LEFT)

        self.listbox_2 = tk.Listbox(self.frame3)
        self.listbox_2.pack()

        self.frame3_delete_box = ttk.Frame(self.frame3)
        self.frame3_delete_box.pack(pady=10)

        self.btn_delete_2 = ttk.Button(self.frame3_delete_box, text='Sil')
        self.btn_delete_2.pack(side=tk.LEFT)

        self.btn_delete_all_2 = ttk.Button(self.frame3_delete_box, text='Hepsini Sil')
        self.btn_delete_all_2.pack(side=tk.LEFT) 

app = App()
app.mainloop()