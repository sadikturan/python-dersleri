from tkinter import *
import wikipedia

window = Tk()
window.title('Wilipedia Api')

def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)

def search():
    wikipedia.set_lang("tr")
    result = wikipedia.page(my_entry.get())
    print(result.content)
    clear()
    my_text.insert(0.0, result.content)

my_label_frame =  LabelFrame(window, text="Search Wikipedia")
my_label_frame.pack(padx=20,pady=20, fill=X)

my_entry = Entry(my_label_frame)
my_entry.pack(padx=20, pady=20, fill=X)

text_frame = Frame(window)
text_frame.pack(padx=20, fill=X)

vertical_scroll = Scrollbar(text_frame, orient='vertical')
vertical_scroll.pack(side=RIGHT, fill=Y)

horizontal_scroll = Scrollbar(text_frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)

my_text = Text(text_frame, yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set, wrap='none')
my_text.pack(fill=X)

vertical_scroll.config(command=my_text.yview)
horizontal_scroll.config(command=my_text.xview)

button_frame = Frame(window)
button_frame.pack(pady=10)

search_button = Button(button_frame, text='Search', font=("Arial", 20), padx=10, pady=3, command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text='Clear', font=("Arial", 20), padx=10, pady=3, command=clear)
clear_button.grid(row=0, column=1, padx=20)

window.mainloop()