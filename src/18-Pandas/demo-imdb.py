import pandas as pd

df = pd.read_csv("datasets/imdb.csv")

# 1- Dosyada hakkındaki bilgiler.
result = df
result = df.columns
result = df.info

# 2- ilk 5 kaydı gösterin
result = df.head()

# 3- ilk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kaydı gösterin
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece Movie_Title kolonunu alın.
result = df["Movie_Title"]

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
result = df["Movie_Title"].head()

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
result = df[["Movie_Title","Rating"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
result = df[["Movie_Title","Rating"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.
result = df[5:20][["Movie_Title","Rating"]].head()

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)


# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.

result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

# 13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyiniz.  

result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]

print(result)
print(df.columns)