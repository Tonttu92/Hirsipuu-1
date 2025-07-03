from random import choice
class Sanatiedosto:
    def __init__(self):
        self.sana = None
        
    def valitse_sana_tiedostosta(self):
        sanat = []
        with open("sanat.txt") as tiedosto:
            for sana in tiedosto:
                sana = sana.replace("\n","")
                sanat.append(sana)
        valittu = choice(sanat)
        self.sana =valittu
        return valittu
    
    def arvauksien_maara(self):
        arvaukset = len(self.sana)
        return int(arvaukset)


class Pelinlogiikka:
    def __init__(self, sana):
        self.sana = sana
        self.arvaukset = set()
        self.yritykset = Sanatiedosto.arvauksien_maara(self)

    def arvaa(self, arvaus):
            arvaus = arvaus.lower()
            if not arvaus.isalpha():
                return "Anna vain kirjaimia."

            if len(arvaus) == 1:
                if arvaus in self.arvaukset:
                    return "Olet jo arvannut tämän kirjaimen."
                self.arvaukset.add(arvaus)
                    
                if arvaus in self.sana:
                    return "Kirjain on sanassa."
                
                else:
                    self.yritykset -=1
                    return "Väärä kirjain"
                
            else:
                if arvaus == self.sana:
                    self.arvaukset.update(self.sana)
                    return "Oikea sana"
                else:
                    self.yritykset -= 1
                    return f"väärä sana!! Sana ei ollut \"{arvaus}\"."

          
    def tilanne(self):
        return [kirjain if kirjain in self.arvaukset else "_" for kirjain in self.sana]

    def loppu(self):
            if self.yritykset == 0:
                return True, f"HÄVISIT! Oikea sana oli: {self.sana}"

            if all(k in self.arvaukset for k in self.sana):
                return True, f"Onneksi olkoon! Arvasit sanan oikein: {self.sana}"    
                
            return False, ""

class Hirsipuu:
    def __init__(self):
        sana = Sanatiedosto.valitse_sana_tiedostosta(self)
        self.peli = Pelinlogiikka(sana)

    def kaynnista(self):
        print("Tervetuloa pelaamaan Hirsipuuta!")
        while True:
            print("sana: ", " ".join(self.peli.tilanne()))
            print(f"Yrityksiä jäljellä: {self.peli.yritykset}")
            arvaus = input("Arvaa kirjain tai koko sana: ")
            vastaus = self.peli.arvaa(arvaus)
            print(vastaus)
            
            loppu, viesti = self.peli.loppu()
            if loppu:
                print(viesti)
                break
        

# Pelin käynnistys:
peli = Hirsipuu()
peli.kaynnista()
