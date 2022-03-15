"""
    Rolul acestei functii este de a determina elementul majoritar(care apare de mai mult de n / 2 ori)

    Parametrii de intrare:

        l - lista de numere
        n - numarul de numere

    Parametrii de iesire:

        maj - elementul majoritar, daca acesta este -1 inseamna ca nu a fost gasit un element majoritar
"""


def determina_element_majoritar(l, n):
    dict = {}

    maj = -1

    for i in range(0, n):

        if l[i] not in dict:

            dict[l[i]] = 1

        else:

            dict[l[i]] += 1

            if dict[l[i]] > n / 2:
                maj = l[i]
                return maj

    return maj


# Rolul acestei functii este de a testa functia ce determina elementul majoritar dintr-o lista de numere

def test_element_majoritar():
    assert determina_element_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2], 11) == 2
    assert determina_element_majoritar([1, 2, 3], 3) == -1
    assert determina_element_majoritar([2, 2, 2, 2, 4, 4, 4, 4, 4], 9) == 4
    assert determina_element_majoritar([1, 7, 7], 3) == 7
    assert determina_element_majoritar([1, 1, 1, 2, 2, 2], 6) == -1


"""
    Rolul acestei functii este de a reprezenta main-ul problemei 6
    in aceasta metoda este citit numarul de elemente, lista de numere si 
    este afisat elementul majoritar daca acesta exista
"""


def main():
    n = int(input("Introduceti numarul de elemente din lista: "))

    l = []

    for i in range(0, n):
        nr = int(input("Introduceti un element al listei: "))
        l.append(nr)

    print("Elementul majoritar al listei este " + str(determina_element_majoritar(l, n)))


test_element_majoritar()
main()
