# users.csv
# FirstName, LastNane
# Sadık,Turan
# Çınar,Turan

# 1- add_user() isminde 2 parametre alan fonksiyon. 
import csv

def add_user(first_name, last_name):
    with open("users.csv","a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name,last_name])

# add_user("Emel","Turan")

# 2- get_users() isminde tüm bilgileri getiren fonksiyon.

def get_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for user in csv_reader:
            print(f'{user["FirstName"]} {user["LastName"]}')

# get_users()

# 3- get_user() isminde firstname ve lastname bilgisine göre kaydın indeksini getiren fonksiyon.

def find_user(first_name,last_name):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        for (index,row) in enumerate(csv_reader):
            if (row[0]==first_name) and (row[1]==last_name):
                return index
        return -1

print(find_user("Sena","Turan"))
