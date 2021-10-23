def findChilds(numbers, pos) -> int:
    #print((" " * pos) + str(numbers[pos]))
    ending = 0
    end = 4
    isEnd = True
    if pos >= len(numbers) - 3 and pos < len(numbers):
        end = len(numbers) - pos
    for i in range(1, end):
        if numbers[pos + i] - numbers[pos] == 1 or numbers[pos + i] - numbers[pos] == 2 or numbers[pos + i] - numbers[pos] == 3:
            ending += findChilds(numbers, pos + i)
            isEnd = False
    if isEnd:
        ending = 1
    return ending

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

numbers.insert(0, 0)
#numbers.append(numbers[len(numbers) - 1])

oups = findChilds(numbers, 0)

print(oups)

#Fermeture du fichier
file.close()
