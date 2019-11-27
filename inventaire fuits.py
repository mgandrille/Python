inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
    ]
# met les quantités en premier
inventaire_trie = [(qte, fruit) for fruit, qte in inventaire]

print(inventaire_trie)  # vérifie l'affichage

inventaire = inventaire_trie.sort(reverse = True)  # trie dans l'ordre croissant
inventaire = [(fruit, qte) for qte, fruit in inventaire_trie]  # remet la liste avec les fruits en premier

print(inventaire)  # affiche le résultat final
