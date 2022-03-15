import copy
import random
from random import randint
from utils.utils import generateNewValue


class Chromosome:
    """
    Aceasta este clasa Chromosome ce retine atributele specifice unui cromozom si metodele aferente acestuia
    """

    def __init__(self, network, problParam=None):
        """
        Constructorul clasei noastre
        :param network: graful retelei curente
        :param problParam: parametrii de care are nevoie cromozomul nostru
        """
        self.__problParam = problParam
        self.__repres = self.init_repres(network)
        self.__fitness = 0.0

    def init_repres(self, network):
        """
        Aceasta functie initializeaza un cromozom dupa urmatoarea regula, toate nodurile au la inceput comunitatea -1
        si pentru fiecare nod fara comunitate i se atribuie o comunitate atat lui cat si vecinilor lui
        :param network: graful nostru
        :return: reprezentarea initiala
        """
        mat = network['mat']

        l = [-1 for _ in range(0, len(mat))]

        pos = 0
        done = False

        while not done:

            done = True

            com = randint(self.__problParam['min'], self.__problParam['max'])

            l[pos] = com

            for i in range(0, len(mat)):

                if mat[pos][i] == 1:
                    l[i] = com

            for j in range(0, len(mat)):

                if l[j] == -1:
                    pos = j
                    done = False
                    break

        return l

    @property
    def repres(self):
        """
        Get method pt repres
        :return: reprezentarea cromozomului
        """
        return self.__repres

    @property
    def fitness(self):
        """
        Get method pt fitness
        :return: fitness ul cromozomului
        """
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        """
        Set method pt reprezentare
        :param l: reprezentarea noua
        """
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        """
        Set method pt fitness
        :param fit: fitness ul nou
        """
        self.__fitness = fit

    def crossover(self, c, network):
        """
        Aceasta este functia de incrucisare ce foloseste modelul propus de Tasgin si Bingol - one way crossover
        :param c: cromozomul cu care incrucisam cromozomul curent
        :param network: graful nostru
        :return: noul cromozom rezultat prin incrucisarea celor 2 cromozomi
        """
        r = randint(0, len(self.__repres) - 1)

        child = []

        for i in range(0, len(self.__repres)):

            if self.__repres[i] == self.__repres[r]:

                child.append(self.__repres[i])

            else:

                child.append(c.__repres[i])

        c1 = Chromosome(network, self.__problParam)

        c1.__repres = child

        return c1

    def mutation(self, pm):
        """
        Aceasta este functia ce se ocupa cu mutatia unui cromozom
        :param pm: probabilitatea de mutatie(redundanta)
        """
        pos = randint(0, len(self.__repres) - 1)
        self.__repres[pos] = generateNewValue(self.__problParam['min'], self.__problParam['max'])

        """
        # Mutatie random resetting
        # o gena e schimbata(cu prob pm) intr-o alta valoare
        
        for pos in range(len(self.__repres)):

            prob = random.uniform(0, 1)

            if prob <= pm:

                self.__repres[pos] = generateNewValue(self.__problParam['min'], self.__problParam['max'])"""

    def __str__(self):
        """
        String method
        :return: chromosome as string
        """
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        """
        Reprezinta obiectele clasei ca string
        :return: obiectul ca string
        """
        return self.__str__()

    def __eq__(self, c):
        """
        Metoda ce compara un obiect cu altul dupa valoarea fitness-ului
        :param c: cromozomul cu care l comparam pe cel curent
        :return: True(egale) / False(Diferite)
        """
        return self.__repres == c.__repres and self.__fitness == c.__fitness
