# numéro choisi par le joueur
def num_joueur():
        n=1
        while n!=0:
                num_joueur = input("Sur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
                num_joueur = int(num_joueur)
                if num_joueur > 49 :                        
                        print("Le numéro choisi n'existe pas, veuillez en choisir un autre !")
                        n=1
                else :
                        num_joueur=int(num_joueur)
                        n=0     

# définir la couleur du numéro
def couleur(n):
        if  n %2 == 0 :
                couleur == True   #noir= numéros pairs
                print("Et c'est un numéro noir (pair)")
        else :
                couleur == False  #rouge= numéros impairs
                print("Et c'est un numéro rouge (impair)")

# définir les gains
def gains():
        import math
        if jeu != num_joueur :
            if (jeu %2 == 0 and num_joueur %2 == 0) or (jeu %2 != 0 and num_joueur %2 != 0):
#            if couleur(jeu) == couleur(num_joueur) :
                gain = math.ceil(mise * 0.5)
                print("\n Vous avez misé sur la bonne couleur, vous gagnez ", gain, "$")
            else:
                gain = 0
                print("\n Loupé, Vous venez de perdre votre mise !")
        else:
                gain = 3 * mise
                print("\n Votre gain est de 3 fois votre mise, soit ", gain, "$")
 

# ****** programme du jeu de la roulette **********
print("Bienvenue au ZCasino, voici le jeu de la Roulette !")
import random
import math
a = input("\nAvec quelle somme d'argent souhaitez vous jouer ? ")
a = int(a)
j=1
while j != 0 :
    #num_joueur()
    num_joueur = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
    num_joueur = int(num_joueur)
    # choisir sa mise
    mise = input("Quelle somme souhaitez vous miser sur ce numéro ? : ")
    mise = int(mise)
    print("\n Votre mise est de ", mise, "$ sur le numéro ", num_joueur, "\n")
    # lance la roulette
    print("A vos jeux... La roulette est lancée... \n")
    jeu=random.randrange(50)
    print("Le numéro gagnant est le numéro ", jeu)
    #couleur(jeu)
    #   gains()
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
    print("Et vous avez au total ", a, " $")
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

