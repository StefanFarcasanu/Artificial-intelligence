"""
    Aceasta functie se ocupa cu determinarea indexului liniei care contine cele mai multe elemente egale cu 1

    Parametrii de intrare:

        mat - matricea ce contine elementele noastre
        n - numarul de linii
        m - numarul de coloane

    Parametrii de iesire:

        indice - indicele liniei ce contine cei mai multi de 1, in cazul in care nu se gaseste niciun 1 in matrice
                 o sa fie returnat 0
"""


def determina_linie_maxima(mat, n, m):
    indice = 0
    maxim = -1

    for i in range(0, n):

        for j in range(0, m):

            if mat[i][j] == 1:

                size = m - j

                if size > maxim:
                    maxim = size
                    indice = i

                break

    return indice


"""
    Rolul acestei metode este de a testa functia ce determina indexul liniei care contine cele mai multe elemente de 1
"""


def test_linie_maxima():
    assert determina_linie_maxima([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], 3, 5) == 1
    assert determina_linie_maxima([[0, 0, 0], [0, 1, 1], [1, 1, 1]], 3, 3) == 2
    assert determina_linie_maxima([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 3) == 0
    assert determina_linie_maxima([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3, 3) == 0
    assert determina_linie_maxima([[0, 1], [1, 1]], 2, 2) == 1


"""
    In functia main sunt citite numarul de linii si de coloane si matricea noastra, dupa care este afisat indicele 
    liniei ce contine cele mai multe valori de 1 
"""


def main():
    n = int(input("Introduceti numarul de linii: "))
    m = int(input("Intrdocueti numarul de coloane: "))

    mat = []

    for i in range(0, n):

        line = []

        for j in range(0, m):
            nr = int(input("Introduceti numarul de pe linia " + str(i) + " si coloana " + str(j) + ": "))
            line.append(nr)

        mat.append(line)

    print("Indicele liniei ce contine cele mai multe valori de 1 este " + str(determina_linie_maxima(mat, n, m)))


test_linie_maxima()
main()
