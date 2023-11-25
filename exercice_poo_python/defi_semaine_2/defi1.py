
class defi1:

    #declaration du constructeur
    def __init__(self,nombre_depart):
        self.nombre_depart = nombre_depart
    
    ## methode pour aller a +10

    def affiche(self):
        nombre_arrive = self.nombre_depart + 10
        for i in range(self.nombre_depart + 1,nombre_arrive):
            print(i)
# creation de l'objet
nombre = defi1(int(input('Entrer le nombre de départ : ')))
nombre.affiche()