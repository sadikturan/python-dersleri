import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    database = "node-app"
)

mycursor = mydb.cursor()


