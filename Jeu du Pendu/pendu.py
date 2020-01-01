# -*-coding:utf-8 -*

# ************* Programme du jeu du Pendu ***************


import os
import random
import donnees

# Paramétrage global
debug = True
paramNbEssaisPossibles = 8
# Fin paramétrage global

print("Bienvenue dans le jeu du Pendu ! \n")

# ***** fonction pour les joueurs *****
#def joueur():
joueur = donnees.joueur
score_final = donnees.score

NomCorrect = False
while NomCorrect == False:
#    joueur=open("donnees.py","a")
    pseudo = input("Quel est votre nom ? ").capitalize()  #on met automatiquement le pseudo avec une majuscle au début
    pseudo = 'Anonyme' if len(pseudo) == 0 else pseudo

    try:
        str(pseudo) != False
    except ValueError :
        print("Il y a une erreur, êtes vous certain de votre frappe ?")
    else :
        if pseudo in joueur :
            print("Bon retour {} ! Votre score précédent est de ? points. ".format(pseudo))
        else:
            joueur.append(pseudo)
            score_final.append(0)
            print ("Bonjour {}, vous n'avez pas de score enregistré".format(pseudo))
        NomCorrect = True

# ***** enregistrement des joueurs *****
#fonctions.joueur()
# ***** recherche aléatoire du mot dans liste données *****
print("\nL'ordinateur va choisir aléatoirement un mot à découvrir.\n\
      Vous avez {} chances pour y arriver ! \n\
      C'est parti...".format(paramNbEssaisPossibles))
      
listeMotsPossibles = donnees.motsPossibles

motADecouvrir=listeMotsPossibles[random.randrange(len(listeMotsPossibles))]
if (debug) : 
    print("Debug - Le mot est : {}".format(motADecouvrir))

nombreLettresRestantesATrouver = len(motADecouvrir)
print("\nLe mot mystère comporte {} lettres à trouver :".format(len(motADecouvrir)))


tabMotADecouvrir = [ lettre for lettre in motADecouvrir]   # *** extraire le mot sous forme de liste par lettre
tabMotEtoiles = [" * " for lettre in motADecouvrir]   # *** remplace les lettres par une *

print(*tabMotEtoiles)
print("\nA vous de le trouver ! ")
essaisRestants = paramNbEssaisPossibles
while essaisRestants > 0 :
    lettreChoisie = ""
    while(len(lettreChoisie) != 1) :
        lettreChoisie = input("\nTapez une lettre : ").lower()

    nbOccurencesLettreChoisie = motADecouvrir.count(lettreChoisie)
    try :
        rech_lettre = tabMotADecouvrir.index(lettreChoisie)  
    except ValueError :
        try :
            lettreChoisie != int(lettreChoisie)
        except ValueError :
            print("Cette lettre n'est pas dans le mot mystère")
            essaisRestants = essaisRestants -1
            print("Il vous reste {} coups".format(essaisRestants))
            coup_rest = essaisRestants
        else :
            print("Etes vous sûr de votre frappe ?")
    else :
        # *** si lettre ds mot, remplacer * par lettre et pas d'impact sur nb de chances
        if nombreLettresRestantesATrouver > 1 :
            i=0
            while i != nbOccurencesLettreChoisie :
                rech_lettre = tabMotADecouvrir.index(lettreChoisie)
                tabMotADecouvrir[rech_lettre] = "*"
                tabMotEtoiles[rech_lettre] = " {} ".format(lettreChoisie)
                i += 1
            nombreLettresRestantesATrouver = nombreLettresRestantesATrouver - nbOccurencesLettreChoisie
        else :
            print("\nBravo, vous avez trouvé le mot mystere : {}".format(motADecouvrir))
            break
        print(*tabMotEtoiles)
        print("Il vous reste {} coups".format(essaisRestants))
# *** score
score = essaisRestants
if essaisRestants == 0 :
    print("\nVous avez perdu ! Le mot était : {}".format(motADecouvrir))
print("\n{}, votre score est de : {} points".format(pseudo, score))
# score final à enregister
# score final = initial + score partie


os.system("pause")   # met en pause le système Windows
