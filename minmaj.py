# Écrivez un programme Python qui accepte une chaîne de caractères de
# l'utilisateur et affiche le nombre de majuscules et de minuscules.

def majmin(x: str):
    maj = min = 0
    for c in x:
        if c.islower():
            min += 1
        elif c.isupper():
            maj += 1
    x = f"{maj} majuscules, {min} minuscules"
    return x
