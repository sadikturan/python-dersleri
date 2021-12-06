from termcolor import colored

# sonuc = dir(termcolor)
# sonuc = help(termcolor)
sonuc = colored("Merhaba",color="green",on_color="on_yellow")
sonuc = colored("Merhaba",color="green",on_color="on_yellow",attrs=["bold"])

print(sonuc)