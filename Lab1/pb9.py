"""
    Rolul acestei functii este de a realiza matricea de sume a submatricilor ce incep in punctul [0, 0] si se termina in [i, j]

    Paranetrii de intrare:

        mat - matricea initiala
        n - numarul de linii
        m - numarul de coloane

    Parametrii de iesire:

        a - matricea rezultat
"""


def determinare_matrice_suma(mat, n, m):
    a = []

    for i in range(0, n):
        a.append([0] * m)

    a[0][0] = mat[0][0]

    # initalizam prima linie
    for j in range(1, m):
        a[0][j] = a[0][j - 1] + mat[0][j]

    # initializam prima coloana
    for i in range(1, n):
        a[i][0] = a[i - 1][0] + mat[i][0]

    # calculam restul matricii folosind formula a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + mat[i][j]

    for i in range(1, n):

        for j in range(1, m):
            a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + mat[i][j]

    return a


"""
    Rolul acestei metode este de a determina suma unei submatrici folosind formula
    
        suma = matSuma[x2, y2] - matSuma[x1 - 1][y2] - matSuma[x2][y1 - 1] + matSuma[x1 - 1][y1 - 1]
    
        unde (x1, y1) sunt coordonatele coltului din stanga sus a matricii
             (x2, y2) sunt coordonatele coltului din dreapta jos a matricii
             
    Parametrii de intrare:
    
        matSuma - matricea sumelor
        x1 - coordonata x a coltului din stanga sus          
        y1 - coordonata y a coltului din stanga sus          
        x2 - coordonata x a coltului din dreapta jos          
        y2 - coordonata y a coltului din dreapta jos
        
    Parametrii de iesire:
    
        suma - reprezentand suma submatricii determinate de cele 2 puncte
          
"""


def determina_suma_submatrice(matSuma, x1, y1, x2, y2):
    suma = matSuma[x2][y2]

    if x1 - 1 >= 0:
        suma -= matSuma[x1 - 1][y2]

    if y1 - 1 >= 0:
        suma -= matSuma[x2][y1 - 1]

    if x1 - 1 >= 0 and y1 - 1 >= 0:
        suma += matSuma[x1 - 1][y1 - 1]

    return suma


"""
    Rolul acestei metode este de a determina suma subamatricii determinate de fiecare pereche de noduri din lista de perechi
    
    Parametrii de intrare:
    
        mat - matricea initiala
        n - numarul de linii
        m - numarul de coloane
        perechi - lista de perechi de noduri
        nrPerechi - numarul de perechi
        
    Parametrii de iesire:
    
        rez - lista cu valoarea fiecarei submatrice determinata de fiecare pereche de noduri   
"""


def determina_suma_submatrice_pentru_perechi(mat, n, m, perechi, nrPerechi):
    matSuma = determinare_matrice_suma(mat, n, m)  # calculam matricea suma

    rez = []

    for i in range(0, nrPerechi):
        pereche = perechi[i]  # pereche = [ [x1, y1], [x2, y2] ]

        suma = determina_suma_submatrice(matSuma, pereche[0][0], pereche[0][1], pereche[1][0], pereche[1][1])

        rez.append(suma)

    return rez


def test_suma_submatrice():
    mat = [[0, 2, 5, 4, 1],
           [4, 8, 2, 3, 7],
           [6, 3, 4, 6, 2],
           [7, 3, 1, 8, 3],
           [1, 5, 7, 9, 4]]

    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[1, 1], [3, 3]], [[2, 2], [4, 4]]], 2) == [38, 44]
    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[2, 0], [4, 1]]], 1) == [25]
    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[0, 3], [1, 4]]], 1) == [15]
    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[2, 2], [2, 2]]], 1) == [4]
    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[0, 0], [0, 0]]], 1) == [0]
    assert determina_suma_submatrice_pentru_perechi(mat, 5, 5, [[[0, 0], [4, 4]]], 1) == [105]


"""
    In functia main o sa se realizeze:
    
        - citirea numarului de linii n
        - citirea numarului de coloane m
        - citirea matricii n * m
        - citirea numarului de perechi
        - citirea perechiilor de noduri
        - afisarea sumei submatricilor corespunzatoarea fiecarei perechi de noduri
"""


def main():
    n = int(input("Introduceti numarul de linii: "))
    m = int(input("Introduceti numarul de coloane: "))

    mat = []

    for i in range(0, n):

        line = []

        for j in range(0, m):
            nr = int(input("Introduceti numarul de pe linia " + str(i) + " si coloana " + str(j) + ": "))
            line.append(nr)

        mat.append(line)

    nr_perechi = int(input("Introduceti numarul de perechi: "))

    lista_perechi = []

    for i in range(0, nr_perechi):
        pereche = []
        print("Perechea " + str(i + 1))
        x1 = int(input("Introduceti coordonata x a coltului stanga sus: "))
        y1 = int(input("Introduceti coordonata y a coltului stanga sus: "))
        x2 = int(input("Introduceti coordonata x a coltului dreapta jos: "))
        y2 = int(input("Introduceti coordonata y a coltului dreapta jos: "))

        pereche.append([x1, y1])
        pereche.append([x2, y2])

        lista_perechi.append(pereche)

    rez = determina_suma_submatrice_pentru_perechi(mat, n, m, lista_perechi, nr_perechi)

    for i in range(0, nr_perechi):
        print("Pentru perechea " + str(lista_perechi[i]) + " suma submatricii determinate de elemente este " + str(rez[i]))


test_suma_submatrice()
main()