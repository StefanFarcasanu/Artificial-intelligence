import copy
from random import randint


def generateNewValue(lim1, lim2):
    """
    Aceasta functie se ocupa cu generarea unei valori random in intervalul lim1 si lim2
    :param lim1: limita inferioara a intervalului
    :param lim2: limita superioara a intervalului
    :return: un numar intreg ales aleator in intervalul [lim1, lim2]
    """
    return randint(lim1, lim2)


# evaluate the quality of previous communities inside a network
# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/modularity.pdf

def modularity(communities, param):
    """
    Aceasta este functia de modularitate ce se ocupa cu calcularea modularitatii unui graf daca acesta are o anume
    impartire in comunitati
    :param communities: repartizarea nodurilor in comunitati
    :param param: graful nostru
    :return:
    """
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    comm_size = param['communitySize']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)

    penalty = 0

    # Penalizam solutiile ce nu contin k comunitati
    if len(set(communities)) != comm_size: #

            # in functie de diferenta dintre nr de comunitati dorite si nr de comunitati avute in solutia curenta
            # o sa penalizam fitness ul solutiei
            penalty = 1 * (comm_size - len(set(communities)))

    return Q * 1 / M - penalty


# Aceasta functie a fost gasita in pdf - pag 8 (17)
def fitness1(community, network):
    """
    Aceasta este o functie alternativa pentru fitness, ce nu calculeaza modularitatea
    :param community: distributia comunitatilor curenta
    :param network: graful nostru
    :return: scorul pentru comunitatea curenta
    """
    mat = network['mat']

    #multime = set(copy.deepcopy(community))

    multime = set()

    for elem in community:

        multime.add(elem)

    suma = 0.0

    # parcurgem comunitatile noastre
    for c in multime:

        scor = 0.0 # scorul comunitatii curente

        for i in range(len(community)): # parcurgem toate nodurile

            # daca nodul i apartine comunitatii curente verificam cate noduri adiacente cu acesta apartin comunitatii
            # si cate nu apartin
            if community[i] == c:
                scorIn = 0.0 # ki in
                scorOut = 0.0 # ki out

                for j in range(len(community)):

                    if mat[i][j] > 0.0:

                        if community[j] == c:

                            scorIn += 1.0 # daca apartine incrementam in

                        else:

                            scorOut += 1.0 # daca nu apartine incrementam out

                scor += scorIn / (scorIn + scorOut) # scorul pentru comunitatea curenta conform formulei

        suma += scor # adaugam scorul comunitatii la scorul final

    # nu uitam de penalty
    if len(multime) != network['communitySize']:

        suma = -1

    return suma

# Aceasta functie a fost gasita in pdf - pag 8 (15)
def fitness2(community, network):
    """
        Aceasta este o functie alternativa pentru fitness, ce nu calculeaza modularitatea
        :param community: distributia comunitatilor curenta
        :param network: graful nostru
        :return: scorul pentru comunitatea curenta
        """
    mat = network['mat']

    multime = set()

    for elem in community:
        multime.add(elem)

    suma = 0.0

    # parcurgem fiecare comunitate
    for c in multime:

        # initializam suma pe comunitatea curenta
        suma_c = 0

        # nr de elemente din comunitatea curenta
        ct = 0

        # nr de muchii din comunitatea curenta
        muchii_comunitate = 0

        # determinam numarul de noduri din comunitatea curenta si nr de muchii din comunitatea curenta
        for i in range(len(mat)):

            if community[i] == c:

                ct += 1

                for j in range(len(mat)):

                    if community[j] == c and mat[i][j] == 1:

                            muchii_comunitate += 1


        for i in range(len(mat)):

            # daca nodul i apartine comunitatii curente
            if community[i] == c:

                # calculam ce e in paranteza
                suma_i = 0

                # daca j apartine comunitatii adaugam la suma noastra mat[i][j]
                for j in range(len(mat)):

                    if community[j] == c:

                        suma_i += mat[i][j]

                suma_i /= ct # nu uitam ca trb sa impartim cu nr de elemente din comunitatea curenta

                suma_c += suma_i # adaugam la suma comunitatii curente

        suma_c /= ct # impartim tot la nr de elemente din comunitatea curenta

        suma_c *= muchii_comunitate # si inmultim cu nr de muchii din comunitatea curenta

        suma += suma_c

    # nu uitam de penalty
    if len(multime) != network['communitySize']:

        suma = -1

    return suma