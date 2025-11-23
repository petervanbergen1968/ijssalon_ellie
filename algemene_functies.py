def mijn_functie_1(a):
    return a * a

mijn_functie_1 = [2, 4, 10, 12]
print(mijn_functie_1)


def mijn_functie_2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst

print(mijn_functie_2(12.3, 3))
print(mijn_functie_2(12.2, 2.1))
print(mijn_functie_2(10.5, 5.5))
print(mijn_functie_2(100.20, 20))