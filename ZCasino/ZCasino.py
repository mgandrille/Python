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
                print("\n Votre gain est de la moitié de votre mise, soit ", gain, "$")
            else:
                gain = 0
                print("\n Vous venez de perdre votre mise !")
        else:
                gain = 3 * mise
                print("\n Votre gain est de 3 fois votre mise, soit ", gain, "$")
        if gain != 0:
            cagnotte = mise + gain
            print("\n\nVous repartez avec ", cagnotte, "$ \n\n")

# ****** programme du jeu de la roulette **********
print("Bienvenue au ZCasino, voici le jeu de la Roulette !")
import random
j=0
while j != 1 :
    #num_joueur()
    num_joueur = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
    num_joueur = int(num_joueur)
    # choisir sa mise
    mise = input("Quelle somme souhaitez vous miser ? : ")
    mise = int(mise)
    print("\n Votre mise est de ", mise, "$ sur le numéro ", num_joueur, "\n")
    # lance la roulette
    print("A vos jeux... La roulette est lancée... \n")
    jeu=random.randrange(50)
    print("Le numéro gagnant est le numéro ", jeu)
    couleur(jeu)
    gains()
    r=input(" Voulez vous rejouer ? (O / N) ")
    if r == "O" or r == "o" :
        j=0
    else:
        print("Au revoir et à bientôt au ZCasino ")
        j=1

