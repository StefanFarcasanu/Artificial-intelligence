# prerequisites
import copy
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def determine_edges_to_be_eliminated(edges):
    """
        Rolul acestei functii este de a determina muchiile ce urmeaza a fi eliminate dupa ce a fost calculata valoarea
        de betweenness pentru fiecare

        Parametrii de intrare:

            edges - un dictionar ce contine pentru fiecare muchie numarul de aparitii

        Parametrii de iesire:

            list_of_index - o lista de tupluri ce contine cheile muchiilor ce urmeaza a fi eliminate
    """
    maximum_val = 0

    list_of_index = []

    for key in edges:

        val = edges[key]

        if val > maximum_val:

            maximum_val = val
            list_of_index = [key]

        elif val == maximum_val:

            list_of_index.append(key)

    print(maximum_val)
    print(list_of_index)
    print("===========================")

    return list_of_index


def eliminate_edges(edges, edges_copy, network, list_of_index):
    """
        Rolul acestei functii este de a elimina muchiile ce au fost determinate de functia anterioara

        Parametrii de intrare:

            edges - un dictionar ce contine pentru fiecare muchie numarul de aparitii
            edges_copy - o copie a dictionarului de baza pentru muchii
            network - graful curent
            list_of_index - o lista de tupluri ce contine cheile muchiilor ce urmeaza a fi eliminate

        Parametrii de iesire:

            nu avem, dar se modifica graful nostru
    """
    for i in list_of_index:
        edges.pop(i)
        network['matrix'][i[0], i[1]] = 0
        network['matrix'][i[1], i[0]] = 0
        edges_copy.pop(i)

    network['edges'] = copy.deepcopy(edges_copy)


def girvan_newman(network, k):
    """
        Rolul acestei functii este de a calcula componentele unui graf folosindu-ne de metoda lui Girvan Newman

        Parametrii de intrare:

            netwrok - graful nostru

        Parametrii de iesire:

            communities - comunitatile fiecarui nod din graf
    """
    edges_copy = copy.deepcopy(network['edges'])

    while True:

        if len(list(nx.connected_components(nx.from_numpy_matrix(network['matrix'])))) == k:

            break

        elif len(network['edges']) == 0:

            break

        edges = network['edges']

        for i in range(0, network['noNodes'] - 1):

            for j in range(i + 1, network['noNodes']):

                try:

                    paths = [nx.shortest_path(nx.from_numpy_matrix(network['matrix']), source=i, target=j)]

                    for p in paths:

                        index = 0

                        while index + 1 < len(p):
                            e1 = p[index]
                            e2 = p[index + 1]

                            n1 = min(e1, e2)
                            n2 = max(e1, e2)

                            edges[(n1, n2)] += 1

                            index += 1

                except nx.NetworkXNoPath:

                    pass

        # ne pregatim de eliminat muchiile ce au valoarea maxima

        list_of_index = determine_edges_to_be_eliminated(edges)

        eliminate_edges(edges, edges_copy, network, list_of_index)

    # dupa ce am iesit din while inseamna ca avem formate comunitatile

    return nx.connected_components(nx.from_numpy_matrix(network['matrix']))


def greedyCommunitiesDetection(network, k):
    """
        Rolul acestei functii este de a apela functia ce determina comunitatile acestuia

        Parametrii de intrare:

            network - graful nostru

        Parametrii de iesire:

            Apelul functiei girvan_newman - pentru graful nostru
    """

    return girvan_newman(network, k)


def get_network_from_gml(path):
    """
    Rolul acestei functii este de a returna graful descris de un fisier gml
    :param path: path-ul catre fisierul .gml
    :return: network ce este un dictionar ce contine toate datele necesare pentru graful nostru
    """
    graph = nx.read_gml(path, label='id')
    edges_list_from_gml = graph.edges
    number_of_nodes = len(graph.nodes)

    matrix = np.zeros((number_of_nodes, number_of_nodes))

    edges = {}

    for edge in edges_list_from_gml:
        matrix[edge[0], edge[1]] = 1
        matrix[edge[1], edge[0]] = 1
        edges[edge] = 0

    network = {}

    network['matrix'] = matrix
    network['noNodes'] = number_of_nodes
    network['edges'] = edges

    return network


def teste_girvan():
    """
        Rolul acestei functii este de testa algoritmul implementat folosind atat exemple din viata reala cat si exemple
        concepute pe foaie
    """

    # Teste identificate de mine

    print("Running tests...")

    # Cateva exemple mai micute

    # Exemplul 2 (se incepe de la 2 pentru ca initial primul exemplu era cel de la MAP)

    print("Example2 running...")

    ex2_graph = get_network_from_gml("exemple/ex2/ex2.gml")

    ex2_communities = greedyCommunitiesDetection(ex2_graph, 2)

    ex2_list = list(ex2_communities)

    print(ex2_list)

    assert len(ex2_list) == 2

    print("Example 2 passed!\n")

    # Exemplul 3

    print("Example3 running...")

    ex3_graph = get_network_from_gml("exemple/ex3/ex3.gml")

    ex3_communities = greedyCommunitiesDetection(ex3_graph, 2)

    ex3_list = list(ex3_communities)

    print(ex3_list)

    assert len(ex3_list) == 2

    print("Example 3 passed!\n")

    # Exemplul 4

    print("Example4 running...")

    ex4_graph = get_network_from_gml("exemple/ex4/ex4.gml")

    ex4_communities = greedyCommunitiesDetection(ex4_graph, 2)

    ex4_list = list(ex4_communities)

    print(ex4_list)

    assert len(ex4_list) == 2

    print("Example 4 passed!\n")

    # Exemplul 5

    print("Example5 running...")

    ex5_graph = get_network_from_gml("exemple/ex5/ex5.gml")

    ex5_communities = greedyCommunitiesDetection(ex5_graph, 3)

    ex5_list = list(ex5_communities)

    print(ex5_list)

    assert len(ex5_list) == 3

    print("Example 5 passed!\n")

    # Exemplul 6

    print("Example6 running...")

    ex6_graph = get_network_from_gml("exemple/ex6/ex6.gml")

    ex6_communities = greedyCommunitiesDetection(ex6_graph, 3)

    ex6_list = list(ex6_communities)

    print(ex6_list)

    assert len(ex6_list) == 3

    print("Example 6 passed!\n")

    # Graful de la MAP - ex1

    print("MAP graph running...")

    map_graph = get_network_from_gml("exemple/ex1/map.gml")

    map_communities = greedyCommunitiesDetection(map_graph, 2)

    map_list = list(map_communities)

    print(map_list)

    assert len(map_list) == 2

    print("MAP graph passed!\n")

    # Miserables - ex2

    print("Running Miserables...")

    g = nx.read_gml("real/Miserables/lesmis.gml")
    g = nx.convert_node_labels_to_integers(g)
    expected = list(nx.algorithms.community.girvan_newman(g))[0]

    mis = get_network_from_gml("real/Miserables/lesmis.gml")
    mis_comm = greedyCommunitiesDetection(mis, 2)
    rez = list(mis_comm)

    i = 0

    assert len(expected) == len(rez)

    while i < min(len(rez), len(expected)):

        assert expected[i] == rez[i]
        i += 1

    assert i == len(rez)
    assert i == len(expected)

    print("Passed Miserables!\n")
    
    # Wordadj - ex 3

    print("Running Wordadj...")

    g = nx.read_gml("real/wordadj/adjnoun.gml")
    g = nx.convert_node_labels_to_integers(g)
    exp2 = list(nx.algorithms.community.girvan_newman(g))[0]

    rez2 = list(girvan_newman(get_network_from_gml("real/wordadj/adjnoun.gml"), 2))

    i = 0

    assert len(exp2) == len(rez2)

    while i < min(len(rez2), len(exp2)):
        assert exp2[i] == rez2[i]
        i += 1

    assert i == len(rez2)
    assert i == len(exp2)

    print("Passed Wordadj!\n")

    # Enzymes-g10 - ex4

    print("Running Enzymes-g10...")

    g = nx.read_gml("real/enzymes-g10/enzymes-g10.gml")
    g = nx.convert_node_labels_to_integers(g)
    exp3 = list(nx.algorithms.community.girvan_newman(g))[0]

    print(exp3)

    rez3 = list(girvan_newman(get_network_from_gml("real/enzymes-g10/enzymes-g10.gml"), 2))

    print(rez3)

    i = 0

    assert len(exp3) == len(rez3)

    while i < min(len(rez3), len(exp3)):
        assert exp3[i] == rez3[i]
        i += 1

    assert i == len(rez3)
    assert i == len(exp3)

    print("Passed Enzymes-g10!\n")

    # sandi - ex 5

    print("Running Sandi...")

    g = nx.read_gml("real/sandi/sandi_auths.gml")
    g = nx.convert_node_labels_to_integers(g)
    exp4 = list(nx.algorithms.community.girvan_newman(g))[0]
    print(exp4)

    rez4 = list(girvan_newman(get_network_from_gml("real/sandi/sandi_auths.gml"), 2))
    print(rez4)

    i = 0

    assert len(exp4) == len(rez4)

    while i < min(len(rez4), len(exp4)):
        assert exp4[i] == rez4[i]
        i += 1

    assert i == len(rez4)
    assert i == len(exp4)

    print("Passed Sandi!\n")

    # enzymes g105 - ex6

    print("Running Enzymes-g105...")

    g = nx.read_gml("real/enzymes-g105/enzymes_g105.gml")
    g = nx.convert_node_labels_to_integers(g)
    exp5 = list(nx.algorithms.community.girvan_newman(g))[0]

    print(exp5)

    rez5 = list(girvan_newman(get_network_from_gml("real/enzymes-g105/enzymes_g105.gml"), 2))
    print(rez5)

    i = 0

    assert len(exp5) == len(rez5)

    while i < min(len(rez5), len(exp5)):
        assert exp5[i] == rez5[i]
        i += 1

    assert i == len(rez5)
    assert i == len(exp5)

    print("Passed Enzymes-g10!\n")

    # Teste din arhiva reala

    # Dolphins

    print("Dolphins running...")

    dolphins = get_network_from_gml("real/dolphins/dolphins.gml")

    dolphins_communities = greedyCommunitiesDetection(dolphins, 2)

    dolphins_list = list(dolphins_communities)

    print(dolphins_list)

    assert len(dolphins_list) == 2

    print("Dolphins passed!\n")

    # Karate

    print("Karate running...")

    karate = get_network_from_gml("real/karate/karate.gml")

    karate_communities = greedyCommunitiesDetection(karate, 2)

    karate_list = list(karate_communities)

    print(karate_list)

    assert len(karate_list) == 2

    print("Karate passed!\n")

    # Krebs

    print("Krebs running...")

    krebs = get_network_from_gml("real/krebs/krebs.gml")

    krebs_communities = greedyCommunitiesDetection(krebs, 3)

    krebs_list = list(krebs_communities)

    print(krebs_list)

    assert len(krebs_list) == 3

    print("Krebs passed!\n")

    # Football

    print("Football running...")

    football = get_network_from_gml("real/football/football.gml")

    football_communities = greedyCommunitiesDetection(football, 12)

    football_list = list(football_communities)

    print(football_list)

    assert len(football_list) == 12

    print("Football passed!\n")

    print("Tests passed!")


def main():
    """
        In functia main sunt apelate testele
    """
    teste_girvan()


main()
