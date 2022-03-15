from queue import Queue

"""
    Rolul acestei functii este de a genera toate numerele in reprezentare binara din intervalul 1, n

    Parametrii de intrare:

        n - limita superioara a intervalului [1, n]

    Parametrii de iesire:

        l - lista de numere din intervalul [1, n] in reprezentare binara

    Daca ar fi sa gandim aceasta problema ca pe un arbore ar fi
    
                        1
                       / \
                      10 11
                     /\  /\
                100 101 110 111  

    Se poate observa o regula, pentru fiecare nod vecinul stang = nodul curent + 0
                                                  vecinul drept = nodul curent + 1
"""


def determina_numere_binar(n):
    l = []

    queue = Queue()

    queue.put("1")  # adaugam primul numar binar

    for i in range(0, n):
        nr = queue.get()  # scoatem primul element

        l.append(int(nr))

        # adaugam in queue numarul curent + caracterul "0" pentru ca acesta reprezinta partea stanga a nodului curent
        queue.put(nr + "0")

        # adaugam in queue numarul curent + caracterul "1" pentru ca acesta reprezinta partea dreapta a nodului curent
        queue.put(nr + "1")

    return l


# Rolul acestei metode este de a testa functia ce determina numerele din intervalul [1, n] in binar

def test_numere_binar():
    assert determina_numere_binar(2) == [1, 10]
    assert determina_numere_binar(3) == [1, 10, 11]
    assert determina_numere_binar(4) == [1, 10, 11, 100]
    assert determina_numere_binar(5) == [1, 10, 11, 100, 101]
    assert determina_numere_binar(14) == [1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110]


"""
    In functia main, este citit n-ul, dupa care este apelata functia ce calculeaza numerele din intervalul 
    [1,n] in binar, ulterior fiind afisate 
"""


def main():
    n = int(input("Introduceti numarul n: "))

    print("Numerele din intervalul [1, " + str(n) + "] sunt " + str(determina_numere_binar(n)))


test_numere_binar()
main()
