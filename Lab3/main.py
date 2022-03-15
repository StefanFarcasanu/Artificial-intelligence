from random import seed

from utils.chromosome import Chromosome
from utils.utils import modularity, fitness1, fitness2
from GeneticAlgorithm import GA

import networkx as nx
import numpy as np


# pentru a ne fi mai usor sa dam debug
# seed(1)


def determine_the_degrees_of_nodes(graph):
    """
    Aceasta functie se ocupa cu determinarea gradelor nodurilor din graf
    :param graph: graful nostru
    :return: lista ce contine gradele nodurilor
    """
    deg = nx.degree(graph)

    degrees = []

    for d in deg:
        degrees.append(d[1])

    return degrees


def get_graph_from_path(path):
    """
    Aceasta functie se ocupa cu construirea unui dictionar ce ii corespunde unui graf citit ditr-un fisier gml, al
    carui path este primit ca si parametru
    :param path: calea catre fisierul .gml
    :return: dictionarul ce contine toate datele grafului descris in fisierul .gml primit ca si parametru
    """
    g = nx.read_gml(path, label="id")
    degrees = determine_the_degrees_of_nodes(g)
    return {'noNodes': len(g.nodes), 'mat': nx.to_numpy_matrix(g).tolist(), 'noEdges': len(nx.to_edgelist(g)),
            'degrees': degrees}


def determine_communities(network, k, popSize, noGen):
    """
    Aceasta functie determina comunitatile dintr-un graf primit ca si parametru folosind un algoritm genetic
    :param network: un dictionar ce contine toate datele despre graful nostru
    :param k: numarul de comunitati pe care dorim sa le obtinem
    :param popSize: dimensiunea populatiei de cromozomi
    :param noGen: numarul de generatii pe care urmeaza sa le generam
    :return: cel mai bun cromozom ce contine repartizarea fiecarui nod in comunitati
    """
    param = {'popSize': popSize, 'noGen': noGen, 'pm': 0.5, 'pc': 0.5}

    problParam = {'min': 0, 'max': k - 1, 'function': modularity, 'noDim': len(network)}
    #problParam = {'min': 0, 'max': k - 1, 'function': fitness1, 'noDim': len(network)}
    #problParam = {'min': 0, 'max': k - 1, 'function': fitness2, 'noDim': len(network)}

    network['communitySize'] = k

    allBestFitnesses = []
    allAvgFitnesses = []
    generations = []

    ga = GA(network, param, problParam)
    ga.initialisation()
    ga.evaluation()

    bestChromo = None

    for gen in range(param['noGen']):
        potentialSolutionRepres = [c.repres for c in ga.population]
        potentialSolutionFitness = [c.fitness for c in ga.population]

        c = ga.bestChromosome()

        bestSolRepres = c.repres
        bestSolFitness = c.fitness

        allBestFitnesses.append(bestSolFitness)
        allAvgFitnesses.append(sum(potentialSolutionFitness) / len(potentialSolutionFitness))

        generations.append(gen)

        # ga.oneGeneration()
        ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        #print("Best chromose in iteration " + str(gen) + " is " + str(bestChromo))

    return bestChromo


def convert_result_to_list(path, length, index=0):
    """
    Rolul acestei functii este de a converti un fisier real.dat in care se afla raspunsul nostru cu o lista ce contine
    la pozitia i comunitatea de care acesta apartine
    :param path: calea catre fisierul real.dat
    :param length: numarul de noduri din graful nostru
    :param index: acest parametru indica daca indexarea in raspuns este de la 1 sau de la 0
    :return:
    """
    file = open(path, "r")

    lines = file.readlines()

    community = [-1 for _ in range(length)]

    com = 0

    for line in lines:

        numbers = line.strip().split()

        for number in numbers:
            community[int(number) - index] = com

        com += 1

    return community


def test_determine_communities():
    """
    Aceasta este functia ce se ocupa cu rularea testelor pe toate grafurile
    """
    epsilon = 0.05

    print("Running Tests...\n")

    # Real networks

    # Archive

    # Dolphins
    print("Running Dolphins...")
    dolphinsNetwork = get_graph_from_path("real/dolphins/dolphins.gml")
    dolphinsChromo = determine_communities(dolphinsNetwork, 2, 100, 300)
    print(dolphinsChromo)
    dolphinsExpected = convert_result_to_list("real/dolphins/real.dat", len(dolphinsChromo.repres), 1)
    print(dolphinsExpected, end=" Expected Modularity: ")
    print(modularity(dolphinsExpected, dolphinsNetwork))
    #assert(abs(dolphinsChromo.fitness - modularity(dolphinsExpected, dolphinsNetwork)) <= epsilon)
    assert (len(set(dolphinsChromo.repres)) == len(set(dolphinsExpected)))
    print("Finished Dolphins!\n")

    # Karate
    print("Running Karate...")
    karateNetwork = get_graph_from_path("real/karate/karate.gml")
    karateChromo = determine_communities(karateNetwork, 2, 100, 100)
    print(karateChromo)
    karateExpected = convert_result_to_list("real/karate/real.dat", len(karateChromo.repres), 1)
    print(karateExpected, end=" Expected Modularity: ")
    print(modularity(karateExpected, karateNetwork))
    #assert (abs(karateChromo.fitness - modularity(karateExpected, karateNetwork)) <= epsilon)
    assert (len(set(karateChromo.repres)) == len(set(karateExpected)))
    print("Finished Karate!\n")

    # Krebs
    print("Running Krebs...")
    krebsNetwork = get_graph_from_path("real/krebs/krebs.gml")
    krebsChromo = determine_communities(krebsNetwork, 3, 100, 100)
    print(krebsChromo)
    krebsExpected = convert_result_to_list("real/krebs/real.dat", len(krebsChromo.repres), 1)
    print(krebsExpected, end=" Expected Modularity: ")
    print(modularity(krebsExpected, krebsNetwork))
    #assert (abs(krebsChromo.fitness - modularity(krebsExpected, krebsNetwork)) <= epsilon)
    assert (len(set(krebsChromo.repres)) == len(set(krebsExpected)))
    print("Finished Krebs!\n")

    # Football
    print("Running Football...")
    footballNetwork = get_graph_from_path("real/football/football.gml")
    footballChromo = determine_communities(footballNetwork, 12, 100, 2000)
    print(footballChromo)
    footballExpected = convert_result_to_list("real/football/real.dat", len(footballChromo.repres), 1)
    print(footballExpected, end=" Expected Modularity: ")
    print(modularity(footballExpected, footballNetwork))
    #assert (abs(footballChromo.fitness - modularity(footballExpected, footballNetwork)) <= epsilon)
    print(len(set(footballChromo.repres)))
    assert (len(set(footballChromo.repres)) == len(set(footballExpected)))
    print("Finished Football!\n")

    # Teste identificate de mine

    # Miserables
    print("Running Miserables...")
    miserablesNetwork = get_graph_from_path("real/Miserables/lesmis.gml")
    miserablesChromo = determine_communities(miserablesNetwork, 5, 100, 1)
    print(miserablesChromo)
    miserablesExpected = convert_result_to_list("real/Miserables/real.dat", len(miserablesChromo.repres), 0)
    print(miserablesExpected, end=" Expected Modularity: ")
    print(modularity(miserablesExpected, miserablesNetwork))
    #assert (abs(miserablesChromo.fitness - modularity(miserablesExpected, miserablesNetwork)) <= epsilon)
    print(len(set(miserablesChromo.repres)))
    assert (len(set(miserablesChromo.repres)) == len(set(miserablesExpected)))
    print("Finished Miserables!\n")

    # Enzymes-g10
    print("Running Enzymes-g10...")
    enzymesg10Network = get_graph_from_path("real/enzymes-g10/enzymes-g10.gml")
    enzymesg10Chromo = determine_communities(enzymesg10Network, 4, 100, 50)
    print(enzymesg10Chromo)
    enzymesg10Expected = convert_result_to_list("real/enzymes-g10/real.dat", len(enzymesg10Chromo.repres), 0)
    print(enzymesg10Expected, end=" Expected Modularity: ")
    print(modularity(enzymesg10Expected, enzymesg10Network))
    #assert (abs(enzymesg10Chromo.fitness - modularity(enzymesg10Expected, enzymesg10Network)) <= epsilon)
    print(len(set(enzymesg10Chromo.repres)))
    assert (len(set(enzymesg10Chromo.repres)) == len(set(enzymesg10Expected)))
    print("Finished Enzymes-g10!\n")

    # Enzymes-g105
    print("Running Enzymes-g105...")
    enzymesg105Network = get_graph_from_path("real/enzymes-g105/enzymes_g105.gml")
    enzymesg105Chromo = determine_communities(enzymesg105Network, 3, 100, 100)
    print(enzymesg105Chromo)
    enzymesg105Expected = convert_result_to_list("real/enzymes-g105/real.dat", len(enzymesg105Chromo.repres), 0)
    print(enzymesg105Expected, end=" Expected Modularity: ")
    print(modularity(enzymesg105Expected, enzymesg105Network))
    #assert (abs(enzymesg105Chromo.fitness - modularity(enzymesg105Expected, enzymesg105Network)) <= epsilon)
    print(len(set(enzymesg105Chromo.repres)))
    assert (len(set(enzymesg105Chromo.repres)) == len(set(enzymesg105Expected)))
    print("Finished Enzymes-g105!\n")

    # MAP
    print("Running Map...")
    mapNetwork = get_graph_from_path("exemple/ex1/map.gml")
    mapChromo = determine_communities(mapNetwork, 2, 10, 3)
    print(mapChromo)
    mapExpected = convert_result_to_list("exemple/ex1/real.dat", len(mapChromo.repres), 0)
    print(mapExpected, end=" Expected Modularity: ")
    print(modularity(mapExpected, mapNetwork))
    #assert (abs(mapChromo.fitness - modularity(mapExpected, mapNetwork)) <= epsilon)
    print(len(set(mapChromo.repres)))
    assert (len(set(mapChromo.repres)) == len(set(mapExpected)))
    print("Finished Map!\n")

    print("Finished tests!\n")


def main():
    """
    Rolul acestei functii este de a apela functia ce se ocupa cu testarea grafurilor din arhiva si cu testarea 
    grafurilor inspirate din viata reala
    """
    test_determine_communities()


main()
