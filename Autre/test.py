# Solution
class Compte(object):
    Nom = ""
    Prenom = ""
    Solde_initial = 50
    Solde = Solde_initial
    Decouvert_autorisee = 100
    Max_compte = 5000

    def __init__(self, n, p, s):
        self.Nom = n
        self.Prenom = p
        self.Solde = s

    def Consulter_le_solde(self):
        return print(self.Nom + " " + self.Prenom, "=> vous avez : ", self.Solde, " euros dans votre compte.")

    def Crediter_le_compte(self, montant):
        if self.Solde + montant <= self.Max_compte:
            self.Solde = self.Solde + montant
            return True
        else:
            return False

    def Debiter_le_compte(self, montant):
        if self.Solde-montant >= -100:
                return False
        else:
            print("Impossible ! Vous avez atteint votre découvert !")



if __name__ == "__main__":
    compte = Compte("Abdou", "MELIANI", 500)
    print("Menu de votre compte : \n 1. consulter le solde  \n 2. Créditer le compte\n 3. Débiter le compte\n 4. Quitter l'appli \n")
    scan = int(input("Choississez un nombre :"))
    while scan != 4:
        if scan == 1:
            compte.Consulter_le_solde()
        if scan == 2:
            montant = int(input("Entrez le montant que vous voulez créditer : "))
            compte.Crediter_le_compte(montant)
            compte.Consulter_le_solde()
        if scan == 3:
            montant = int(input("Entrez le montant que vous voulez débiter : "))
            compte.Debiter_le_compte(montant)
            compte.Consulter_le_solde()
        scan = int(input("Choississez un nombre SVP:"))
    if scan == 4:
        print("à bientot !")