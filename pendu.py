# -*-coding:Latin-1 -*

# ************* Programme du jeu du Pendu ***************


import os
import random

print("Bienvenue dans le jeu du Pendu ! \n")

# ***** fonction pour les joueurs *****
#def joueur():
j=1
while j!=0:
    joueur=open("donnees.py","a")
    pseudo = input("Quel est votre nom ? ")
    try:
        int(pseudo) == False
    except ValueError :
        print("Il y a une erreur, êtes vous certain de votre frappe ?")
    else :
        joueur.write(pseudo)
        print ("Bonjour", pseudo, ", vous n'avez pas de score enregistré")
        joueur.close()
        j=0

# ***** enregistrement des joueurs *****
#joueur()
# ***** recherche aléatoire du mot dans liste données *****
print("\nL'ordinateur va choisir aléatoirement un mot à découvrir.\n\
      Vous avez 8 chances pour y arriver ! \n\
      C'est parti...")
mot_mystere = ["vision", "bateau", "chouette", "bonjour", "amour", "festival"]
no_mot = random.randrange(5)
#print("index mot", no_mot) #********** A SUPPRIMER ************
m=mot_mystere[no_mot]
print("le mot est :", m) #********** A SUPPRIMER ************
long = len(m)
print("\nLe mot à trouver comporte ", long, " lettres à trouver :")
# *** extraire le mot sous forme de liste par lettre
for lettre in m :
    mon_mot = [ lettre for lettre in m]
#    print("mon mot", mon_mot) #********** A SUPPRIMER ************
    # *** remplacer lettres par *
    mystere = [" * " for lettre in mon_mot]
    print(*mystere)
print("\nA vous de le trouver ! ")
coup = 8
while coup > 0 :
    choix_lettre = input("\nTapez une lettre :   ")
    # *** recherche dans le mot si lettre est présente (1 fois ou plusieurs fois)
    rech_lettre = m.find(choix_lettre)
    compte_lettre = m.count(choix_lettre)
#    print("recherche = ", rech_lettre, "et nb de lettre = ", compte_lettre) #********** A SUPPRIMER ************
    if rech_lettre < 0:
        # *** si pas lettre ds mot, continuer en disant que ce n'est pas la bonne lettre et 1 chance en moins
        print("Cette lettre n'est pas dans le mot mystère")
        coup = coup -1
    else :
        try :
            rech_lettre = mon_mot.index(choix_lettre)  
        except ValueError:
            coup = 0
        else :
            # *** si lettre ds mot, remplacer * par lettre et pas d'impact sur nb de chances
            i=0
            while i != compte_lettre :
                rech_lettre = mon_mot.index(choix_lettre)
                mon_mot[rech_lettre] = "*"
                mystere[rech_lettre] = choix_lettre
                i += 1
            print(*mystere)
                  
# 8 chances pour trouver (boucle)
# si mot trouvé avant => score = 8 - nb de mauvais coups joués
# si mot pas trouvé => perdu ! (score = 0)

# score final à enregister
# score final = initial + score partie


os.system("pause")   # met en pause le système Windows
