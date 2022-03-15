"""
    Rolul acestei functii este de a determina elementul ce se repeta in lista trimisa ca si parametru

    Parametrii de intrare:

        l - lista ce contine elementele noastre
        n - numarul de elemente din lista noastra

    Parametrii de iesire:

        nr - elementul ce se repeta
"""


def determina_element_repetat(l, n):
    suma = sum(l)
    s = (n - 1) * n / 2

    return suma - s


# Rolul acestei functii este de a testa functia ce determina elementul ce se repeta intr-o lista de n elemente

def test_element_repetat():
    assert determina_element_repetat([1, 2, 3, 4, 2], 5) == 2
    assert determina_element_repetat([1, 2, 1], 3) == 1
    assert determina_element_repetat([1, 2, 4, 3, 3], 5) == 3
    assert determina_element_repetat([1, 1, 2, 3], 4) == 1
    assert determina_element_repetat([1, 2, 3, 4, 5, 5], 6) == 5


"""
    Rolul acestei functii este de a reprezenta main-ul problemei 5
    in aceasta metoda este citit n-ul si lista de n elemente, dupa care este calculat
    elementul ce se repeta
"""


def main():
    n = int(input("Introduceti numarul n: "))

    l = []

    for i in range(0, n):
        nr = int(input("Introduceti un element din lista: "))

        l.append(nr)

    print("Elementul ce se repeta in lista noastra este " + str(determina_element_repetat(l, n)))


test_element_repetat()
main()
