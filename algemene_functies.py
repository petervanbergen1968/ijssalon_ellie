a = 2
b = 4
c = 10
d = 12

def mijn_functie_1():
    return (a*a, b*b, c*c, d*d)

print(mijn_functie_1())

import math

def mijn_functie_2(invoer_lijst):
    uitvoer = []
    for a in invoer_lijst:
        if a == 12.3:
            b = 3
        elif a == 12.2:
            b = 2
        elif a == 10.5:
            b = 5
        elif a == 100.20:
            b = 20
        else:
            continue  

        optellen = math.floor(a + b)
        aftrekken = math.floor(a - b)

        product = a * b
        if product >= 100:
            vermenigvuldigen = math.floor(product / 100) * 100
        else:
            vermenigvuldigen = math.floor(product)

        delen = math.floor(a / b)

        uitvoer.append([optellen, aftrekken, vermenigvuldigen, delen])

    return uitvoer

mijn_lijst = [12.3, 12.2, 10.5, 100.20]
print(mijn_functie_2(mijn_lijst))