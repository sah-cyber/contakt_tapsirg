# Mənə Python-da sadə əlaqə kitabçası proqramı lazımdır.
#
# Proqram aşağıdakı funksiyaları yerinə yetirməlidir:
#
# Yeni kontakt əlavə etmək (ad və telefon).
#
# Bütün kontaktları göstərmək.
#
# Ada görə kontakt axtarmaq.
#
# Kontakti silmək.
#
# Proqramdan çıxmaq.
from tkinter.font import names


class  Telefon:
    def __init__(self):
        print("Telefona xow gelmisiniz")

        self.contacts = {}



    def menu(self):

        while True:
            print("""
            Proqrama xow gelmisiniz
            1. Kontakt elave elemek
            2. Kontakt axtarmaq
            3.Kpontakt goster
            4.Kontakti sil
            5.Cixiw
            """)
            daxil = input("Seciminiz: ")

            if daxil == '1':
                self.contakt_add()
            elif daxil == '2':
                self.contact_search()
            elif daxil == '3':
                self.contact_show()

            elif daxil == '4':
                self.contact_dell()
            elif daxil == '5':
                print("sagolun")
                break
            else:
                print("yalnis secim")

    def contakt_add(self):

        name = input("Contact adi: ")
        number = input("Telefon nomresi: ")
        self.contacts[name] = number
        print("Kontakt qeyd edildi")





    def contact_search(self):
        search = input("Axtarmaq istediyiniz ad: ")

        if search in self.contacts:
            print(f"{search} :{self.contacts[search]}")

        else:
            print("Kontakt tapilmadi")

    def contact_show(self):
        print("Kontaktlar")
        for c,n in self.contacts.items():
            print(f"Adi: {c}-- Nomre {n}")

    def contact_dell(self):
        sil = input("Silmek istediyiniz kontakt: ")

        if sil in self.contacts:
            del self.contacts[sil]
            print(f" qeyd etdiyiniz {sil} kontakti silindi")

        else:
            print("kontakt tapilmadi")


iwle = Telefon()

iwle.menu()