
# variable qui va recuperer les 20 nombres
nombres = []

#une boucles qui va permettre d'enter les 20 nombres
for i in range(5):
    print("Entrez le nombre numéro ",i+1,": ")
    nombres.append(int(input()))
print(nombres)
# la fonction max qui va extraire le plus grand nombre
print("Le plus grand de ces nombres est : ", max(nombres))
print("C’était le nombre numéro ", nombres.index(max(nombres)) + 1)
