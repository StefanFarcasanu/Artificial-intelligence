from random import randint

from utils.chromosome import Chromosome


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
        self.__network = network

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
            c = Chromosome(self.__network, self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        """
        Metoda folosita pentru evaluarea populatiei
        """
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__network)

    def worstChromosome(self):
        """
        Determina cel mai rau cromozom(worst fitness)
        :return: cel mai rau cromozom
        """
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness < worst.fitness:
                worst = c
        return worst

    def bestChromosome(self):
        """
        Determina cel mai bun cromozom(best fitness)
        :return: cel mai bun cromozom
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
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        """
        Aceasta este metoda ce genereaza la fiecare generatie noua cate o noua populatie de cromozomi
        """
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__network)
            off.mutation(self.__param['pm'])
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        """
        Aceasta este metoda ce retine doar cei mai puternici cromozomi
        """
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__network)
            off.mutation(self.__param['pm'])
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        """
        E ceva incorect la functia asta
        """
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2, self.__network)
            off.mutation(self.__param['pm'])
            off.fitness = self.__problParam['function'](off.repres, self.__network)
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off