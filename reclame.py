from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {prijs_na_korting:.2f} euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal = round(totaal, 2)
    btw_bedrag = round(btw_bedrag, 2)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarovern {btw_bedrag:.2f} euro btw betaald dient te worden."
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

print(inkomsten_totaal(inkomsten))


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer = f"De laagste inkomen deze week is {laagste} euro en de hoogste inkomen is {hoogste} euro."
    return uitvoer

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print(laag_en_hoog(mijn_lijst))


def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomen deze week zijn {gemiddelde:.2f} euro."
    return uitvoer

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print(gemiddelde(mijn_lijst))


def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig(mijn_lijst))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print(combinatie(mijn_lijst))