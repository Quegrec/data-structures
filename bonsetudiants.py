def bonsetudiants(etudiants: dict):
    bons_etudiants: dict = {nom: note for nom,
                            note in etudiants.items() if note >= 15}
    return bons_etudiants
