
class defi2:

    def __init__(self,nombre_depart):
        self.nombre_depart = nombre_depart

    # la methode qui fait la table de muiltiplication
    def table_multi(self):

        for i in range(1,10):
            print(self.nombre_depart, " X " , i , " = ",self.nombre_depart*i)

table = defi2(int(input("Entrer le nombre : ")))
table.table_multi()