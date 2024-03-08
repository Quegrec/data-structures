from stock_inventory import remaining_stock


def test_remaining_stock():
    assert remaining_stock(
                    {"1": {"nom": "banane", "prix": 1.5, "quantite": 10},
                     "2": {"nom": "pomme", "prix": 2, "quantite": 5},
                     "3": {"nom": "poire", "prix": 2.5, "quantite": 4},
                     "6": {"nom": "fraise", "prix": 3, "quantite": 0},
                     "5": {"nom": "orange", "prix": 0.8, "quantite": 0},
                     "4": {"nom": "kiwi", "prix": 3, "quantite": 0}}) == [
                        {"nom": "fraise", "prix": 3, "quantite": 0},
                        {"nom": "kiwi", "prix": 3, "quantite": 0},
                        {"nom": "orange", "prix": 0.8, "quantite": 0}
                        ]
