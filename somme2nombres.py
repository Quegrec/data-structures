def sommeint(nombreun: str, nombredeux: str):
    dict_nombre = {
        "zéro": 0, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
        "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10
    }
    # nombreun = input(str("Entrez un chiffre en toutes lettres : "))
    # nombredeux = input(str("Entrez un autre chiffre en toutes lettres : "))
    somme = dict_nombre[nombreun] + dict_nombre[nombredeux]
    return somme


def sommestr(nombreun: str, nombredeux: str):
    dict_nombre = {
        "zéro": 0, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
        "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10
    }
    nombre_dict = {
        0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
        6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"
    }
    # nombreun = input(str("Entrez un chiffre en toutes lettres : "))
    # nombredeux = input(str("Entrez un autre chiffre en toutes lettres : "))
    somme = dict_nombre[nombreun] + dict_nombre[nombredeux]
    return nombre_dict[somme]
