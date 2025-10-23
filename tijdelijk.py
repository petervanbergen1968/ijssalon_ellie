prijzen_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen_dictionary["aardbei"] * 0.8
reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
reclame_tekst2 = reclame_tekst[:63]
woorden = reclame_tekst2.split()

for el in woorden:
    if len(el) >= 5:
        el = el.upper()
    else:
        el = el.lower()

    for letter in el:
        print(letter)
    print()