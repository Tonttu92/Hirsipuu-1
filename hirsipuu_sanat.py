import random

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