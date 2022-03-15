"""
    Rolul acestei functii este de a determina al k-lea cel mai mare element dintr-o lista l primita ca si parametru

    Parametrii de intrare:

        l - lista de numere
        k - indicele elementului maximal cautat
        n - lungimea listei l

    Parametrii de iesire:

        maxk - al k-lea cel mai mare element, acesta este -1 in cazul in care k nu e in [0,n]
"""


def determina_k_maxim(l, k, n):
    maxk = -1

    sorted_l = sorted(l, reverse=True)

    if k < 0 or k > n:

        return maxk

    else:

        maxk = sorted_l[k - 1]
        return maxk


# Rolul acestei functii este de a testa functia ce determina al k-lea cel mai mare element dintr-o lista de numere

def test_determina_k_maxim():
    assert determina_k_maxim([4, 2, 12, 8], 2, 4) == 8
    assert determina_k_maxim([7, 4, 6, 3, 9, 1], 2, 6) == 7
    assert determina_k_maxim([1, 2, 3, 4], 4, 4) == 1
    assert determina_k_maxim([6, 7, 8, 9], 9, 4) == -1
    assert determina_k_maxim([1, 2, 3, 4, 5, 6, 7], 2, 7) == 6


"""
    In functia main se citesc:
        n - numarul de numere din lista
        l - lista de numere
        k - indicele elementului maximal cautat
        
    Dupa care se afiseaza al k-lea cel mai mare element din lista noastra de numere    
"""


def main():
    n = int(input("Introduceti numarul de elemente din lista: "))

    l = []

    for i in range(0, n):
        nr = int(input("Introduceti un element al listei: "))
        l.append(nr)

    k = int(input("Introduceti indicele elementului maximal cautat: "))

    print("Al " + str(k) + "-lea cel mai mare element este " + str(determina_k_maxim(l, k, n)))


test_determina_k_maxim()
main()
