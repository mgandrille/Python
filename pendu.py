# -*-coding:Latin-1 -*

# ************* Programme du jeu du Pendu ***************


import os
import random

print("Bienvenue dans le jeu du Pendu ! \n")

dico_pseudo = dict()
pseudo = input("Quel est votre nom ? ")
# recherche si existe dans liste données
for pseudo in dico_pseudo:
    # si oui, rappel du score
    if pseudo == True :
        for pseudo, score in dico_pseudo.items():
            print("Bon retour {} , votre score est actuellement de {} points".format(pseudo, score))
        # si non, créer le pseudo associé à un score nul dans fichier score
    else :
        pseudo["pseudo"] = 0
        print ("Bonjour", pseudo, ", vous n'avez pas de score enregistré")
# recherche aléatoire du mot dans liste données
print("\nL'ordinateur va choisir aléatoirement un mot à découvrir.\n\
      Vous avez 8 chances pour y arriver ! \n\
      C'est parti...")
mot_mystere = ["vision", "bateau", "chouette", "bonjour", "amour", "festival"]
no_mot = random.randrange(5)
#print("index mot", no_mot) #********** A SUPPRIMER ************
m=mot_mystere[no_mot]
print("le mot est :", m) #********** A SUPPRIMER ************
long = len(m)
print("\nLe mot à trouver comporte ", long, " lettres à trouver")
# remplacer lettres par *
for lettre in m :
    mot_mystere = m.split(lettre)
    print(mot_mystere) #********** A SUPPRIMER ************
    print(" {} ".format("*")) 
print("A vous de le trouver ! ")
#boucle à mettre (variable = coups joués)
chance = 8
while chance > 0 :
    choix_lettre = input("\nTapez une lettre :   ")
    # recherche dans le mot si lettre est présente (1 fois ou plusieurs fois)
    rech_lettre = m.find(choix_lettre)
    compte_lettre = m.count(choix_lettre)
    print("recherche = ", rech_lettre, "et nb de lettre = ", compte_lettre) #********** A SUPPRIMER ************
    if rech_lettre < 0:
        # si oui, continuer en disant que ce n'est pas la bonne lettre et 1 chance en moins
        print("Cette lettre n'est pas dans le mot mystère")
        chance = chance -1
    else :
        # si non, remplacer * par lettre et pas d'impact sur nb de chances
        for choix_lettre in m :
            p1 = m[:rech_lettre].replace(choix_lettre, "*")
            p2 = m[rech_lettre:].replace(choix_lettre, "*")
            mot_mystere = p1 + m[rech_lettre] + p2
            print(mot_mystere)
#            print(" {} ". format(mystere))
            chance = chance
                  
# 8 chances pour trouver (boucle)
# si lettre OK => 
# si lettre KO => 
# si mot trouvé avant => score = 8 - nb de mauvais coups joués
# si mot pas trouvé => perdu ! (score = 0)

# score final à enregister
# score final = initial + score partie


os.system("pause")   # met en pause le système Windows
