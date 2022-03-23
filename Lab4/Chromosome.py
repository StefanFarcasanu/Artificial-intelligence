from random import randint
from utils import generateNewValue
import numpy as np


class Chromosome:
    """
        Aceasta este clasa Chromosome ce retine atributele specifice unui cromozom si metodele aferente acestuia
    """

    def __init__(self, problParam=None):
        """
        Constructorul clasei noastre
        :param problParam: parametrii de care are nevoie cromozomul nostru
        """
        self.__problParam = problParam
        self.__repres = np.random.permutation(problParam['max'] + 1)
        self.__fitness = 0.0

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

    def crossover(self, c):
        """
        Aceasta este functia de incrucisare ce foloseste modelul propus in curs
        :param c: cromozomul cu care incrucisam cromozomul curent
        :param network: graful nostru
        :return: 2 cromozmoi rezultati prin incrucisarea celor 2 cromozomi
        """
        poz1 = generateNewValue(self.__problParam['min'], self.__problParam['max'])
        poz2 = generateNewValue(self.__problParam['min'], self.__problParam['max'])

        if poz1 > poz2:
            poz1, poz2 = poz2, poz1

        newRepresentation = [-1 for _ in range(len(self.__repres))]

        secondRepresentation = [-1 for _ in range(len(self.__repres))]

        for i in range(poz1, poz2 + 1):
            newRepresentation[i] = self.__repres[i]
            secondRepresentation[i] = c.__repres[i]

        next_position = 0

        next_position_second = 0

        if poz2 + 1 < len(self.__repres):
            next_position = poz2 + 1
            next_position_second = poz2 + 1

        # partea din dreapta a cromozomului 2
        for i in range(next_position, len(self.__repres)):

            if c.__repres[i] not in newRepresentation:

                newRepresentation[next_position] = c.__repres[i]

                next_position += 1

                if next_position == len(self.__repres):
                    next_position = 0

            if self.__repres[i] not in secondRepresentation:

                secondRepresentation[next_position_second] = self.__repres[i]

                next_position_second += 1

                if next_position_second == len(self.__repres):
                    next_position_second = 0

        # parcurgem de la inceput al 2 lea cromozom de la inceput
        for i in range(0, len(c.__repres)):

            if c.__repres[i] not in newRepresentation:

                newRepresentation[next_position] = c.__repres[i]

                next_position += 1

                if next_position == len(self.__repres):
                    next_position = 0

            if self.__repres[i] not in secondRepresentation:

                secondRepresentation[next_position_second] = self.__repres[i]

                next_position_second += 1

                if next_position_second == len(self.__repres):
                    next_position_second = 0

        child = Chromosome(self.__problParam)

        child.__repres = newRepresentation

        second_child = Chromosome(self.__problParam)

        second_child.__repres = secondRepresentation

        return child, second_child

    def mutation(self):
        """
        Aceasta este functia ce se ocupa cu mutatia unui cromozom
        :param pm: probabilitatea de mutatie(redundanta)
        """
        pos1 = randint(0, len(self.__repres) - 1)
        pos2 = randint(0, len(self.__repres) - 1)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

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

    def compare_lists(self, l1, l2):
        """
        Aceasta metoda se ocupa cu compararea a 2 liste
        :param l1: prima lista
        :param l2: a 2 a lista
        :return: True daca sunt egale, altfel False
        """

        equal = True

        for i in range(0, len(l1)):

            if l1[i] != l2[i]:

                equal = False

        return equal

    def __eq__(self, c):
        """
        Metoda ce compara un obiect cu altul dupa valoarea fitness-ului
        :param c: cromozomul cu care l comparam pe cel curent
        :return: True(egale) / False(Diferite)
        """
        return self.compare_lists(self.__repres, c.__repres) and self.__fitness == c.__fitness


