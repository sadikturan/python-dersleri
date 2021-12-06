# list
# tuple
# dictionary
# sets => indekslenemez, sıralanamaz

meyveler = { "elma","kiraz","kavun","üzüm" }
sebzeler = { "bezelye","soğan" }

# sonuc = meyveler[0] indekslenemez
sonuc = "elma" in meyveler
meyveler.add("karpuz")
meyveler.update(["vişne","kavun"])

sonuc = len(meyveler)
# meyveler.remove("karpuzz") # KeyError
# meyveler.discard("karpuz")

# sonuc = meyveler.pop()
# meyveler.clear()

sonuc = meyveler.union(sebzeler)

# for x in meyveler:
#     print(x)

print(sonuc)
