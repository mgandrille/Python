class Jeu:
    """Classe définissant le jeu de la roulette caractérisé par :
    - un numéro gagnant ;
    - un gain rapporté    """

    
    def __init__(self, gagne, gain):
        """Constructeur de notre classe"""
        self.gagne = gagne
        self.gain = gain

    import random
    def num_gagnant(self, gagne):
        """Méthode permettant de selectionner le numéro gagnant   """
        gagne = random.randrange(50)
        print("Le numéro gagnant est le numéro ", gagne)
        
    import math
    def gain_partie(self, somme_misee, numero_mise, gain):
        """Méthode permettant de déterminer le gain du joueur en fonction du numéro gagnant  """
        if gagne != numero_mise :
            if (gagne %2 == 0 and numero_mise %2 == 0) or (gagne %2 != 0 and numero_mise %2 != 0):
                gain = math.ceil(mise * 0.5)
                print("\n Vous avez misé sur la bonne couleur, vous gagnez ", gain, "$")
                somme_finale = somme_misee + gain
            else:
                gain = 0
                print("\n Loupé, Vous venez de perdre votre mise !")
                gain = - somme_misee
        else:
            gain = 3 * somme_misee
            print("\n Votre gain est de 3 fois votre mise, soit ", gain, "$")

