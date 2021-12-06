import sqlite3
import pandas as pd

# df = pd.read_csv('datasets/sample.csv')
# df = pd.read_json('datasets/sample.json',encoding="UTF-8")
# df = pd.read_excel("datasets/sample.xlsx")

connection = sqlite3.connect("datasets/sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)

print(df)