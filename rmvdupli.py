def remove_duplicates(liste):
    listV2 = []
    for nbr in liste:
        if nbr not in listV2:
            listV2.append(nbr)
    return listV2
