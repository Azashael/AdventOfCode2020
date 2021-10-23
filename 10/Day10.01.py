#Ouverture du fichier
file = open("Day10.txt")
#Lecture et copie des données
data = file.read()
#Mise en forme des données
numbers = list(map(int, data.split('\n')))

# Trie des chargeurs dans l'ordre
numbers.sort()
countOne = 0
countTwo = 0
countThree = 0
start = 0

for i in range(0, len(numbers)):
    if numbers[i] - start == 1:
        countOne += 1
    elif numbers[i] - start == 3:
        countThree += 1
    else:
        countTwo += 1
    start = numbers[i]

countThree += 1

print("Difference one : " + str(countOne) + " ; Difference Three : " + str(countThree))
print(countOne * countThree)

#Fermeture du fichier
file.close()
