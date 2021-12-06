class Pet:
    cinsler = ["kedi","köpek","kuş"]

    def __init__(self,isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.isim = isim
        self.cins = cins

    def set_cins(self,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.cins = cins

boncuk = Pet("Boncuk","kedi")
pasa = Pet("Paşa","köpek")
mavis = Pet("Maviş","kuş")

mavis.set_cins("aslan")

# boncuk.cinsler.append("balık")
# pasa.cinsler.append("balık")

# print(Pet.cinsler)
# print(boncuk.cinsler)
# print(pasa.cinsler)