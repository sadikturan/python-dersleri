import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis = 1)
result = df.drop(["column1","column2"], axis = 1)
result = df.drop('a', axis = 0)
result = df.drop(['a','b','h'], axis = 0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna() # axis = 0 => satıra
result = df.dropna(axis = 1) # axis = 1 => sütuna
result = df.dropna(how = "any")
result = df.dropna(how = "all")
result = df.dropna(subset  = ["column1","column2"], how = "all")
result = df.dropna(subset  = ["column1","column2"], how = "any")
result = df.dropna(thresh = 2)
result = df.dropna(thresh = 3) # en az sayıda normal veri

result = df.fillna(value = 'no input')
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))

print(result)
