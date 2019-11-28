# ****** programme du jeu de la roulette **********
print("Bienvenue au ZCasino, voici le jeu de la Roulette !")
import random
import math
# Somme disponible au départ
a = input("\nAvec quelle somme d'argent souhaitez vous jouer ? ")
while type(a) != int:
        try:
                int(a) == True
        except ValueError:
                print("Il y a une erreur, êtes vous certain de votre frappe ?")
                a = input("Avec quelle somme d'argent souhaitez vous jouer ? ")
        else :
                a = int(a)
                if a < 1 :
                        print("Vous ne pouvez pas jouer sans argent !")
                        a = input("Avec quelle somme d'argent souhaitez vous jouer ? ")
# début du jeu
j=1
while j != 0 :
        # numéro choisi par le joueur
        num_joueur = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
        while type(num_joueur) != int:
                try:
                        int(num_joueur) == True
                except ValueError:
                        print("Il y a une erreur, êtes vous certain de votre frappe ?")
                        num_joueur = input("Sur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
                else :
                        num_joueur = int(num_joueur)
                        if num_joueur < 0 or num_joueur > 49:
                                print("Le numéro choisi n'existe pas, veuillez en choisir un autre !")
                                num_joueur = input("Sur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
        # choisir sa mise
        mise = input("\nQuelle somme souhaitez vous miser sur ce numéro ? : ")
        while type(mise) != int :
                try:
                        int(mise) == True
                except ValueError :
                        print("Etes vous certain de votre frappe ?")
                        mise = input("Quelle somme souhaitez vous miser sur ce numéro ? : ")
                else :
                        mise = int(mise)
                        if mise <0:
                                print("Vous ne pouvez pas miser un nombre négatif !")
                                mise = input("Quelle somme souhaitez vous miser sur ce numéro ? : ") 
                        elif mise >a:
                                print("Vous n'avez pas assez d'argent !")
                                mise = input("Quelle somme souhaitez vous miser sur ce numéro ? : ")
        print("\n Votre mise est de ", mise, "$ sur le numéro ", num_joueur, "\n")
        # lance la roulette
        print("A vos jeux... La roulette est lancée... \n")
        jeu=random.randrange(50)
        print("Le numéro gagnant est le numéro ", jeu)
        # résultats et gains
        if jeu != num_joueur :
                if (jeu %2 == 0 and num_joueur %2 == 0) or (jeu %2 != 0 and num_joueur %2 != 0):
                        gain = math.ceil(mise * 0.5)
                        print("\n Vous avez misé sur la bonne couleur, vous gagnez ", gain, "$")
                        a = a + gain
                else:
                        gain = 0
                        print("\n Loupé, Vous venez de perdre votre mise !")
                        a = a - mise
        else:
                gain = 3 * mise
                print("\n Votre gain est de 3 fois votre mise, soit ", gain, "$")
                a = a + gain
        print("Il vous reste donc ", a, " $ pour continuer de jouer.")
        # possibilité de rejouer ou non
        if a == 0:
                print("\nVous n'avez plus d'argent ! Au revoir et à bientôt au ZCasino ")
                j=0
        else:
                r=input(" Voulez vous rejouer ? (O / N) ")
                if r == "O" or r == "o" :
                        j=1
                else:
                        print("Au revoir et à bientôt au ZCasino ")
                        j=0

