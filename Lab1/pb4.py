"""
    Rolul acestei metode este de a determina cuvintele ce apar o singura data intr-un text

    Parametrii de intrare:

        text - sirul de cuvinte separate prin spatiu

    Paremetrii de iesire:

        result - lista de cuvinte ce apar o singura data in text
"""


def determina_cuvinte_unice(text):
    l = text.split()

    m = {}

    for i in range(0, len(l)):

        if l[i] not in m:

            m[l[i]] = 1

        else:

            m[l[i]] += 1

    result = []

    for key in m:

        if m[key] == 1:
            result.append(key)

    return result


# Rolul acestei metode este de a testa functia ce determina cuvintele ce apar o singura data intr-un text

def test_cuvinte_unice():
    assert determina_cuvinte_unice("ana are ana are mere rosii ana") == ["mere", "rosii"]
    assert determina_cuvinte_unice("ana are are ana") == []
    assert determina_cuvinte_unice("popa are mere mari") == ["popa", "are", "mere", "mari"]
    assert determina_cuvinte_unice("") == []
    assert determina_cuvinte_unice("ana Ana aNa") == ["ana", "Ana", "aNa"]


# Aceasta este functia main in care este citit sirul de cuvinte si in care sunt afisate cuvintele ce apar o singura data

def main():
    s = input("Introduceti sirul de cuvinte: ")

    print("Cuvintele ce apar o singura data in sirul nostru sunt " + str(determina_cuvinte_unice(s)))


test_cuvinte_unice()
main()
