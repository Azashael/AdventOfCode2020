#Ouverture du fichier
file = open("Day3.txt")
grid = file.read().splitlines()
#value : nombre d'arbre rencontré sur la route du tobbogan
value = 0
#i : la colonne où l'on est
col = 0
#On lit les données du document
for x in grid:
    if x[col % len(x)] == '#':
        value = value + 1
    col = col + 3

    #print(i)
print(value)

#Fermeture du fichier
file.close()
