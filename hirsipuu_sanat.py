from random import choice

def lue_sanat_tiedostosta(tiedoston_nimi="sanat.txt"):
    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            sanat = [rivi.strip().lower() for rivi in tiedosto if rivi.strip()]
        return sanat
    except FileNotFoundError:
        print("Virhe: sanalistaa ei löytynyt.")
        return []

def valitse_sana(sanalista):
    if not sanalista:
        return None
    return random.choice(sanalista)

class Pelinlogiikka:
    def __init__(self, sana):
        self.sana = sana
        self.arvaukset = set()
        self.yritykset = Sanatiedosto.arvausten_maara(self)

    def arvaa(self, arvaus):
        arvaus = arvaus.lower()
        if not arvaus.isalpha():
            return f"Anna vain kirjaimia."
        
        if len(arvaus) == 1:
            if arvaus in self.arvaukset:
                return f"Olet jo arvannut tämän kirjaimen."
            self.arvaukset.add(arvaus)
            if arvaus in self.sana:
                return f"Kirjain on sanassa."
            else:
                self.yritykset -=1
                return f"Väärä kirjain"
        else:
            if arvaus == self.sana:
                self.arvaukset.update(self.sana)
                return f"Oikea sana"
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