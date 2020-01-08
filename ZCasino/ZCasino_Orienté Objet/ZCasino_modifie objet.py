import os
import random
import math
import ZCasino_jeu
import ZCasino_joueur


# ****** programme du jeu de la roulette **********
print("Bienvenue au ZCasino, voici le jeu de la Roulette !")

# choix du joueur
pseudo = 0
porte_monnaie = 0
numero_mise = 0
somme_misee = 0

ZCasino_joueur.Joueur(pseudo, porte_monnaie, numero_mise, somme_misee)

pseudo = input("Quel est votre nom ?")
Joueur.nom_joueur(pseudo)

porte_monnaie = input("\nAvec quelle somme d'argent souhaitez vous jouer ? ")
Joueur.argent_joueur(porte_monnaie)

# début du jeu
j=1
while j != 0 :
        # numéro choisi par le joueur
        numero_mise = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
        num_joueur(numero_mise)
        # choisir sa mise
        somme_misee = input("\nQuelle somme souhaitez vous miser sur ce numéro ? : ")
        mise_joueur(self, somme_misee)
        print("\n Votre mise est de {} $ sur le numéro {} \n".format(mise, num_joueur))
        # lance la roulette
        print("A vos jeux... La roulette est lancée... \n")
        gagne=random.randrange(50)
        print("Le numéro gagnant est le numéro ", gagne)
        # gains
        Jeu(gagne, gain)
        gain_partie(somme_misee, numero_mise, gain)
        porte_monnaie = porte_monnaie + gain
        print("Il vous reste donc ", porte_monnaie, " $ pour continuer de jouer.")
        # possibilité de rejouer ou non
        if porte_monnaie == 0:
                print("\nVous n'avez plus d'argent ! Au revoir et à bientôt au ZCasino ")
                j=0
        else:
                r=input(" Voulez vous rejouer ? (O / N) ")
                if r == "O" or r == "o" :
                        j=1
                else:
                        print("Au revoir et à bientôt au ZCasino ")
                        j=0

os.system("pause")   # met en pause le système Windows
