from math import sqrt

"""
    Rolul acestei functii este de a calcula distanta euclidiana dintre cele 2 puncte trimise ca si paremetru
    aplicand formula radical( (a2 - a1) ^ 2 + (b2 - b1) ^ 2 )
    
    Parametrii de intrare:
    
        a1 - coordonata x a primului punct
        b1 - coordonata y a primului punct
        a2 - coordonata x a celui de-al doilea punct
        b2 - coordonata y a celui de-al doilea punct
    
    Paramaterii de iesire:
    
        dist - reprezentand distanta dintre punctele (a1, b1) si (a2, b2)
"""


def distanta_euclidiana(a1, b1, a2, b2):
    return sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)


# Rolul acestei functii este de a testa functia ce determina distanta euclidiana intre 2 puncte

def test_distanta_euclidiana():
    assert distanta_euclidiana(-7, -4, 17, 6.5) == 26.196373794859472
    assert distanta_euclidiana(0, 0, 1, 1) == 1.4142135623730951
    assert distanta_euclidiana(-1, 3, -1, 1) == 2
    assert distanta_euclidiana(1, 5, 4, 1) == 5
    assert distanta_euclidiana(1, 0, 5, 0) == 4


"""
    Rolul acestei functii este de a reprezenta main-ul problemei 2
    in aceasta metoda sunt citite cele 2 puncte si calculata diferenta dintre acestea
"""


def main():
    a1 = float(input("Introduceti x-ul primului punct: "))
    b1 = float(input("Introduceti y-ul primului punct: "))
    a2 = float(input("Introduceti x-ul celui de-al doilea punct: "))
    b2 = float(input("Introduceti x-ul celui de-al doilea punct: "))
    dist = distanta_euclidiana(a1, b1, a2, b2)
    print("Distanta dintre cele 2 puncte este " + str(dist))


test_distanta_euclidiana()
main()
