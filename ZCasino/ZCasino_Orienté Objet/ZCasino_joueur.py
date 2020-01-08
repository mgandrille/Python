class Joueur:
    """Classe définissant un joueur de roulette caractérisé par :
    - son pseudo ;
    - son porte monnaie ;
    - un numéro misé
    - une somme misée   """

    
    def __init__(self, pseudo, porte_monnaie, numero_mise, somme_misee):
        """Constructeur de notre classe"""
        self.pseudo = pseudo
        self.porte_monnaie = porte_monnaie
        self.numero_mise = numero_mise
        self.somme_misee = somme_misee

    def nom_joueur(self, pseudo):
        """Méthode permettant de vérifier que le nom du joueur n'est pas un chiffre et de l'afficher   """
        try:
            int(self.pseudo) == True
        except ValueError:
            print("Bienvenue {} sur la table de la Roulette du Zcasino !".format(self.pseudo))
        else:
            print("Il y a une erreur, êtes vous certain de votre frappe ?")
            return

    def argent_joueur(self, porte_monnaie):
        """Méthode permettant de vérifier que le joueur a de l'argent pour jouer"""
        try:
            int(self.porte_monnaie) == True
        except ValueError:
            print("Il y a une erreur, êtes vous certain de votre frappe ?")
            return
        else :
            self.porte_monnaie = int(self.porte_monnaie)
            if self.porte_monnaie < 1 :
                print("Vous ne pouvez pas jouer sans argent !")
                return

    def num_joueur(self, numero_mise):
        """Méthode permettant de vérifier que le joueur a bien misé sur un numéro de la roulette"""
        try:
            int(self.numero_mise) == True
        except ValueError:
            print("Il y a une erreur, êtes vous certain de votre frappe ?")
        else :
            self.numero_mise = int(self.numero_mise)
            if self.numero_mise < 0 or self.numero_mise > 49:
                print("Le numéro choisi n'existe pas, veuillez en choisir un autre !")

    def mise_joueur(self, somme_misee):
        try:
            int(self.somme_misee) == True
        except ValueError :
            print("Etes vous certain de votre frappe ?")
        else :
            self.somme_misee = int(self.somme_misee)
            if self.somme_misee < 0:
                print("Vous ne pouvez pas miser un nombre négatif !")
                return
            elif self.somme_misee > self.porte_monnaie:
                print("Vous n'avez pas assez d'argent !")
                return


