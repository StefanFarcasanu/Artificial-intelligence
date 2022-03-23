from random import randint


def generateNewValue(lim1, lim2):
    """
    Aceasta functie se ocupa cu generarea unei valori random in intervalul lim1 si lim2
    :param lim1: limita inferioara a intervalului
    :param lim2: limita superioara a intervalului
    :return: un numar intreg ales aleator in intervalul [lim1, lim2]
    """
    return randint(lim1, lim2)


def fitnessFunction(community, network):
    """
    Aceasta este functia ce se ocupa cu calcularea fitness-ului unei posibile reprezentari
    :param community: comunitatea pentru care calculam fitness-ul
    :param network: graful nostru
    :return: valoarea numerica ce reprezinta valoarea fitness-ului comunitatii primite ca si parametru
    """

    fitness = 0

    mat = network['mat']

    for i in range(len(community) - 1):

        node1 = community[i]
        node2 = community[i + 1]

        if mat[node1][node2] != 0:

            fitness += mat[node1][node2]

        else:

            fitness += network['penalty']

    s = community[0]
    d = community[-1]

    if mat[s][d] != 0:

        fitness += mat[s][d]

    else:

        fitness += network['penalty']

    return fitness


def fitnessFunctionShortestPath(community, network):
    """
    Rolul acestei functii este de a calcula lungimea drumului intre source si dest
    :param community: ordinea parcurgerii curente a nodurilor
    :param network: dicitonarul ce contine toate datele despre graful nostru
    :param source: nodul de start
    :param dest:  nodul de finish
    :return:
    """
    fitness = 0

    mat = network['mat']

    source = network['source']

    dest = network['dest']

    start = False

    for i in range(0, len(mat) - 1):

        if community[i] == source or community[i] == dest:

            if start is False:

                start = True

            else:

                start = False

        if start is True:

            value = mat[community[i]][community[i + 1]]

            if value != 0:

                fitness += value

            else:

                fitness += network['penalty']

    return fitness
