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
        str(pseudo) != False
    except ValueError :
        print("Il y a une erreur, êtes vous certain de votre frappe ?")
    else :
        joueur.write(pseudo)
        print ("Bonjour", pseudo, ", vous n'avez pas de score enregistré")
        joueur.close()
        score = 0
        j=0

# ***** enregistrement des joueurs *****
#joueur()
# ***** recherche aléatoire du mot dans liste données *****
print("\nL'ordinateur va choisir aléatoirement un mot à découvrir.\n\
      Vous avez 8 chances pour y arriver ! \n\
      C'est parti...")
mot_mystere = ["vision", "bateau", "chouette", "bonjour", "amour", "festival"]
no_mot = random.randrange(6)
m=mot_mystere[no_mot]
print("le mot est :", m) #********** A SUPPRIMER ************
long = len(m)
print("\nLe mot mystère comporte ", long, " lettres à trouver :")
mon_mot = [ lettre for lettre in m]   # *** extraire le mot sous forme de liste par lettre
#print("mon mot", mon_mot) #********** A SUPPRIMER ************
mystere = [" * " for lettre in mon_mot]   # *** remplace les lettres par une *
print(*mystere)
print("\nA vous de le trouver ! ")
essai = 8
while essai > 0 :
    choix_lettre = input("\nTapez une lettre :   ")
    choix_lettre = choix_lettre.lower()
    compte_lettre = m.count(choix_lettre)
    try :
        rech_lettre = mon_mot.index(choix_lettre)  
    except ValueError :
        try :
            choix_lettre != int(choix_lettre)
        except ValueError :
            print("Cette lettre n'est pas dans le mot mystère")
            essai = essai -1
            print("Il vous reste ", essai, " coups")
            coup_rest = essai
        else :
            print("Etes vous sûr de votre frappe ?")
    else :
        # *** si lettre ds mot, remplacer * par lettre et pas d'impact sur nb de chances
        if long > 1 :
            i=0
            while i != compte_lettre :
                rech_lettre = mon_mot.index(choix_lettre)
                mon_mot[rech_lettre] = "*"
                mystere[rech_lettre] = choix_lettre
                i += 1
            long = long - compte_lettre
        else :
            print("\nBravo, vous avez trouvé le mot mystere : ", m )
            break
        print(*mystere)
        print("Il vous reste ", essai, " coups")
# *** score
score = score + coup_rest
if coup_rest == 0 :
    print("\nVous avez perdu !")
print("\n", pseudo, " , votre score est de : ", score, " points")
# score final à enregister
# score final = initial + score partie


os.system("pause")   # met en pause le système Windows
