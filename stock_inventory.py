def remaining_stock(produits: dict):
    rupture = [
        produit for produit in produits.values() if produit["quantite"] == 0
        ]
    rupture.sort(key=lambda produit: produit["prix"], reverse=True)
    rupture.sort(key=lambda produit: produit["nom"])
    return rupture
