# -*-coding:Latin-1 -*

# ************* Programme du jeu du Pendu ***************


import os
import random
import donnees

print("Bienvenue dans le jeu du Pendu ! \n")

# ***** fonction pour les joueurs *****
#def joueur():
joueur = donnees.joueur
score_final = donnees.score
j=1
while j!=0:
#    joueur=open("donnees.py","a")
    pseudo = input("Quel est votre nom ? ")
    pseudo = pseudo.capitalize()  #on met automatiquement le pseudo avec une majuscle au d�but
    try:
        str(pseudo) != False
    except ValueError :
        print("Il y a une erreur, �tes vous certain de votre frappe ?")
    else :
        if pseudo in joueur :
            print("Bon retour {} ! Votre score pr�c�dent est de ? points. ".format(pseudo))
        else:
            joueur.append(pseudo)
            score_final.append(0)
            print ("Bonjour", pseudo, ", vous n'avez pas de score enregistr�")
        j=0

# ***** enregistrement des joueurs *****
#fonctions.joueur()
# ***** recherche al�atoire du mot dans liste donn�es *****
print("\nL'ordinateur va choisir al�atoirement un mot � d�couvrir.\n\
      Vous avez 8 chances pour y arriver ! \n\
      C'est parti...")
#mot_mystere = ["vision", "bateau", "chouette", "bonjour", "amour", "festival"]
mot_mystere = donnees.mot_mystere
no_mot = random.randrange(6)
m=mot_mystere[no_mot]
print("le mot est :", m) #********** A SUPPRIMER ************
long = len(m)
print("\nLe mot myst�re comporte ", long, " lettres � trouver :")
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
            print("Cette lettre n'est pas dans le mot myst�re")
            essai = essai -1
            print("Il vous reste ", essai, " coups")
            coup_rest = essai
        else :
            print("Etes vous s�r de votre frappe ?")
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
            print("\nBravo, vous avez trouv� le mot mystere : ", m )
            break
        print(*mystere)
        print("Il vous reste ", essai, " coups")
# *** score
score = essai
if essai == 0 :
    print("\nVous avez perdu !")
print("\n", pseudo, " , votre score est de : ", score, " points")
# score final � enregister
# score final = initial + score partie


os.system("pause")   # met en pause le syst�me Windows
