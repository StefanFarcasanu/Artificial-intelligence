"""
    Rolul acestei functii este de a calcula produsul scalar a 2 vectori n dimensionali primiti ca si parametru

    Parametrii de intrare:

        v1 - primul vector
        v2 - al doilea vector
        n - dimensiunea celor 2 vectori

    Parametrii de iesire:

        p - produsul celor 2 vectori
"""


def determina_produs_scalar(v1, v2, n):
    p = 0

    for i in range(0, n):
        p += v1[i] * v2[i]

    return p


"""
    Rolul acestei metode este de a testa functia ce returneaza produsul scalar a 2 vectori unidimensionali
"""


def test_produs_scalar():
    assert determina_produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1], 5) == 4
    assert determina_produs_scalar([1, 1], [2, 2], 2) == 4
    assert determina_produs_scalar([1, 1], [0, 0], 2) == 0
    assert determina_produs_scalar([1], [5], 1) == 5
    assert determina_produs_scalar([1, 2, 0], [4, 0, 6], 3) == 4


"""
    In functia main o sa citim dimensiunea fiecarui vector unidimensional dupa care o sa citim cei 2 vectori
    iar dupa citirea acestora o sa calculam produsul lor
"""


def main():
    n = int(input("Introduceti lungimea vectorilor: "))

    v1 = []

    for i in range(0, n):
        nr = int(input("Introduceti numarul din v1: "))
        v1.append(nr)

    v2 = []

    for i in range(0, n):
        nr = int(input("Introduceti numarul din v2: "))
        v2.append(nr)

    print("Produsul celor doi vectori este " + str(determina_produs_scalar(v1, v2, n)))


test_produs_scalar()
main()
