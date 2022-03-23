import random
from random import randint

from Chromosome import Chromosome


class GA:
    """
        Aceasta clasa se ocupa cu definirea algoritmului genetic si cu retinerea atributelor si metodelor aferente acestuia
    """

    def __init__(self, network, param=None, problParam=None):
        """
            Acesta este constructorul clasei noastre

            param - un dictionar ce contine la cheia:
                        - popSize - numarul de cromozomi din generatia curenta
                        - noGen - numarul de generatii generate
                        - pc - probabilitatea de incrucisare
                        - pm - probabilitatea de mutatie

            problParam - un dictionar ce contine la cheia:
                        - function - functia ce determina fitness ul unui cromozom, in cazul nostru o sa fie modularity
                        - min - val min pentru comunitate - 0 in cazul nostru sau 1 depinde de unde decidem sa pornim
                        - max - val max pentru comunitate - n-1 sau n depinde de unde decidem sa plecam
                        - noDim - dimensiunea unui cromozom in cazul nostru o sa fie n
        """
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        self.__network = network;

    @property
    def population(self):
        """
        Get method pentru populatie
        :return: populatia
        """
        return self.__population

    def initialisation(self):
        """
        Metoda folosita pentru initializarea populatiei
        """
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        """
        Metoda folosita pentru evaluarea populatiei
        """
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__network)

    def bestChromosome(self):
        """
        Determina cel mai bun cromozom(best fitness)
        :return: cel mai bun cromozom
        """
        # best = self.__population[0]
        # best_list = [best]
        # for c in self.__population:
        #     if c.fitness < best.fitness:
        #         best = c
        #         best_list = [best]
        #
        #     elif c.fitness == best.fitness:
        #
        #         found = False
        #
        #         for elem in best_list:
        #
        #             if elem == c:
        #
        #                 found = True
        #                 break
        #
        #         if found is False:
        #
        #             best_list.append(c)
        #
        # return best_list

        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromosome(self):
        """
        Determina cel mai rau cromozom(worst fitness)
        :return: cel mai rau cromozom
        """
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        """
        Returnează cel mai puternic cromozom dintre 2 cromozomi alesi la intamplare
        :return: cel mai bun dintre 2 cromozomi
        """
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGenerationElitism(self):
        """
            Aceasta este metoda ce retine doar cei mai puternici cromozomi
        """
        newPop = [self.bestChromosome()]
        newPopSize = len(newPop)
        for _ in range(self.__param['popSize'] - newPopSize):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]

            pc = random.random()

            if pc <= self.__param['pc']:

                off1, off2 = p1.crossover(p2)

                off1.fitness = self.__problParam['function'](off1.repres, self.__network)
                off2.fitness = self.__problParam['function'](off1.repres, self.__network)

                if off1.fitness < off2.fitness:

                    off = off1

                else:

                    off = off2

            else:

                if p1.fitness < p2.fitness:

                    off = p1

                else:

                    off = p2

            pm = random.random()

            if pm <= self.__param['pm']:
                off.mutation()

            newPop.append(off)

        self.__population = newPop
        self.evaluation()
