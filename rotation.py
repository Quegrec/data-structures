def rotateList(liste, rotation):
    for i in range(rotation):
        liste.insert(0, liste.pop())
    return liste
