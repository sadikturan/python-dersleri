import pandas as pd
import numpy as np
fifa_data=pd.read_csv("Pandas/fifa_eda_stats.csv")
fifa_data=pd.DataFrame(fifa_data)
print(fifa_data)
# İlk 10 kaydı getiriniz.
print(fifa_data.head(10))
# Toplam kaç kayıt vardır
print(fifa_data.info)
# Tüm Oyuncuların toplam maaş ortalması nedir.
fifa_data['Wage']=fifa_data['Wage'].str.extract(r'(\d+)').astype(int)
print(f"€{fifa_data['Wage'].mean()}K")
# En yüksek maaaş ne kadardır.
print(fifa_data['Wage'].max())
# En yüksek maaşı Hangi oyuncu alıyor.
result=fifa_data['Wage'].max()
print(fifa_data[fifa_data['Wage']==result]["Name"])
# Yaşı 20-25 aralığında olan futbolcuların ismi ve oynadıkları takım
result=(fifa_data["Age"]>=20)& (fifa_data["Age"]<=25)
print(fifa_data[result].loc[:,['Name','Club','Age']].head(30))
# M. Icardi isimli oyuncunun oynadığı takım hangisidir.
result=fifa_data['Name']=='M. Icardi'
print(fifa_data[result]['Club'])
# Takımlara göre oyuncuların ortalama maaş bilgisi nedir.
result=fifa_data.groupby('Club')['Wage'].mean()
print(result)
# Galatasaray takımının maaş ortalaması

print(fifa_data.groupby('Club')['Wage'].mean()['Galatasaray SK'])
# En çok maaş veren 50 klüp
print(result.sort_values(ascending=False).head(50))
# Kaç Farklı Takım mevcut.
print(fifa_data['Club'].nunique())
# Takımlarda kaç fulbolcu var
print(fifa_data['Club'].value_counts())  # value_counts() :Burada veri iskeletinde belirttiğimiz kolondaki farklı verilerin kaç kez tekrar ettiğini buluruz 
# burada Club yazarak her bir clübun kaç kez tekrar ettiğini buluyoruz ve böylece buda bize o klüpte bulunan oyuncu sayısını veriyor
print(fifa_data['Age'].value_counts()) #Farklı bir örnekle pekiştirelim
# Galatasaray Takımın'da kaç futbolcu var ve Bunları lsiteleyiniz.
result=(fifa_data['Club']=='Galatasaray SK')
print(fifa_data[result])
print(len(fifa_data[fifa_data['Club']=='Galatasaray SK']))
# Galatasaraydaki futbolcuların maaşlarını listeleyiniz.
print(fifa_data[result].loc[:,['Wage','Name']].sort_values('Wage',ascending=False))
# İsminde alex bulunan futbolcular.
print(fifa_data[fifa_data['Name'].str.contains("Alex")])