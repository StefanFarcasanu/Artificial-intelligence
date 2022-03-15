"""
    Clasa Problema11 contine ca si campuri matricea noastra, numarul de linii si numarul de coloane

    Totodata, clasa contine si 3 metode, 2 metode ce o ajuta pe a 3-a sa rezolve problema noastra
"""


class Problema11:
    """
        Constructorul clasei noastre

            Parametrii de intrare:

                matrice - matricea noastra
                lin - numarul de linii
                col - numarul de coloane
    """

    def __init__(self, matrice, lin, col):

        self.matrice = matrice
        self.lin = lin
        self.col = col

    """
        Rolul acestei metode este de a marca cu -1 componentele unui drum ce porneste de pe una din laturile matricii 
        si are valoarea 0. In momentul in care gasim un nod cu valoarea 0, acesta este marcat cu -1, ca facand parte
        dintr-un drum ce incepe dintr-o margine, iar dupa aceea verificam daca vecinii lui sunt egali cu 0, in caz 
        afirmativ continuam deplasarea
        
        Parametrii de intrare:
        
            i - indicele corespunzator liniei elementului nostru
            j - indicele corespunzator coloanei elementului nostru 
            self - campurile clasei noastre
    """

    def umple_aparitiile_lui_0_margine(self, i, j):

        self.matrice[i][j] = -1  # acel nod face parte dintr-o componenta ce incepe din marginea matricii

        if j - 1 > 0 and self.matrice[i][j - 1] == 0:  # verificam el din stanga

            self.umple_aparitiile_lui_0_margine(i, j - 1)

        if i - 1 > 0 and self.matrice[i - 1][j] == 0:  # verificam el de sus

            self.umple_aparitiile_lui_0_margine(i - 1, j)

        if j + 1 < self.col and self.matrice[i][j + 1] == 0:  # verificam in partea dreapta

            self.umple_aparitiile_lui_0_margine(i, j + 1)

        if i + 1 < self.lin and self.matrice[i + 1][j] == 0:  # verificam in partea de jos

            self.umple_aparitiile_lui_0_margine(i + 1, j)

    """
        Rolul acestei metode este de a construi matricea finala, astfel, in matricea noastra se aflau valori de -1, 0, 1
        -1 semnificand faptul ca acel element facea partea dintr-o bucata de 0-uri ce incepe de pe una din muchiile 
        matricii, 0 semnfica elementele ce sunt inconjurate de 1, iar 1 elementele normale. Dupa rularea acestei functii
        in loc de valoarea 0 sa avem valoarea 1 si in loc de valoarea -1 o sa avem valoarea 0
        
        Parametrii de intrare:
        
            self - campurile clasei noastre
    """

    def umple_aparitiile_lui_0_inconjurat(self):

        for i in range(0, self.lin):

            for j in range(0, self.col):

                if self.matrice[i][j] == 0:
                    self.matrice[i][j] = 1

                elif self.matrice[i][j] == -1:
                    self.matrice[i][j] = 0

    """
        Rolul acestei metode este de a rezolva problema noastra, si anume inlocuirea valorilor de 0 inconjurate de 1 cu 
        valoarea 1. Pasii pe care ii aplica aceasta functie sunt:
        
            1) Sunt marcate cu -1 toate sirurile consecutive de 0 ce incep de pe marginea matricii
            2) Este calculata matricea finala cu inlocuirile mentionate anterior
            3) Este returnat acest rezultat
            
        Parametrii de intrare:
        
            self - campurile clasei noastre
            
        Parametrii de iesire:
        
            matrice - reprezentand matricea rezultat        
    """

    def rezolva_problema(self):

        for j in range(0, self.col):

            if self.matrice[0][j] == 0:
                self.umple_aparitiile_lui_0_margine(0, j)

            if self.matrice[self.lin - 1][j] == 0:
                self.umple_aparitiile_lui_0_margine(self.lin - 1, j)

        for i in range(0, self.lin):

            if self.matrice[i][0] == 0:
                self.umple_aparitiile_lui_0_margine(i, 0)

            if self.matrice[i][self.col - 1] == 0:
                self.umple_aparitiile_lui_0_margine(i, self.col - 1)

        self.umple_aparitiile_lui_0_inconjurat()

        return self.matrice


"""
    Rolul acestei functii este de a testa metoda ce se ocupa cu rezolvarea problemei noastre
"""


def test_problema11():
    p = Problema11([[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                    [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]], 8, 10)
    assert p.rezolva_problema() == [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                                    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    p = Problema11([[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [1, 0, 0, 1],
                    [0, 1, 1, 0]], 4, 4)
    assert p.rezolva_problema() == [[0, 1, 1, 0],
                                    [1, 1, 1, 1],
                                    [1, 1, 1, 1],
                                    [0, 1, 1, 0]]

    p = Problema11([[0, 0],
                    [0, 0]], 2, 2)
    assert p.rezolva_problema() == [[0, 0],
                                    [0, 0]]

    p = Problema11([[1, 0],
                    [0, 1]], 2, 2)
    assert p.rezolva_problema() == [[1, 0],
                                    [0, 1]]

    p = Problema11([[0]], 1, 1)
    assert p.rezolva_problema() == [[0]]


"""
    Rolul main-ului este de a citi numarul de linii, de coloane si matricea cu care o sa lucreze functia noastra.
    Dupa ce datele de intrare sunt citite, se realizeaza apelul functiei ce rezolva cerinta data, dupa care este
    afisat pe ecran rezultatul.
"""


def main():
    lin = int(input("Introduceti numarul de linii: "))
    col = int(input("Introduceti numarul de coloane: "))

    mat = []

    for i in range(0, lin):

        line = []

        for j in range(0, col):
            nr = int(input("Introduceti numarul de pe linia " + str(i) + " si coloana " + str(j) + ": "))
            line.append(nr)

        mat.append(line)

    p = Problema11(mat, lin, col)

    print(p.rezolva_problema())


test_problema11()
main()
