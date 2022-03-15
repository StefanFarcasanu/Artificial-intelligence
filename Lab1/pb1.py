"""
    Rolul acestei functii este de a determina cel mai mare cuvant din sirul nostru de cuvinte
    trimis ca si parametru

    Parametrii de intrare:

        s - sirul de cuvinte separate prin spatiu

    Parametrii de iesire:

        max_word - cuvantul maximal, daca acesta este empty atunci sirul a fost vid
"""


def determina_cuvant_maximal(s):
    l = s.split()

    max_word = "empty"

    for i in range(0, len(l)):

        if max_word == "empty":

            max_word = l[i]

        elif l[i] > max_word:

            max_word = l[i]

    return max_word


# Rolul acestei functii este de a testa functia ce calculeaza cuvantul maximal dintr-un sir de cuvinte

def test_cuvant_maximal():
    assert determina_cuvant_maximal("Ana are mere si pere") == "si"
    assert determina_cuvant_maximal("z zz zzz") == "zzz"
    assert determina_cuvant_maximal("a A") == "a"  # literele mici au un cod ascii mai mare decat literele mari
    assert determina_cuvant_maximal("a b c d e ea eb ez") == "ez"
    assert determina_cuvant_maximal("test pentru problema cuvant maximal") == "test"
    assert determina_cuvant_maximal("") == "empty"


"""
    Rolul acestei functii este de a reprezenta main-ul problemei 1
    in aceasta metoda este citit sirul de cuvinte si este afisat cuvantul maximal
"""


def main():
    s = input("Introduceti sirul de cuvinte: ")

    print("Cel mai mare cuvant din sirul nostru este " + determina_cuvant_maximal(s))


test_cuvant_maximal()
main()
