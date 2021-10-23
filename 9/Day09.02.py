def searchFirstNoSum(preambule, numbers) -> int:
    i = preambule
    l = preambule
    j = 0
    k = 0
    maxi = len(numbers)
    valid = False
    calc = 0

    # Pour chaque nombre de preambule à fin
    while i < maxi:
        #print(numbers[i])
        valid = False
        j = i - preambule
        l = i - preambule
        # Pour chaque nombre de 0 à préambule :
        while j < i:
            #print(" J : " + str(j) + " ; " + str(numbers[j]))
            k = l
            while k < i:
                if k == j:
                    k += 1
                    # Pas de re-use
                    continue
                calc = numbers[j] + numbers[k]
                #print("\t K : " + str(k) + " ; " + str(numbers[k]) + " ; " + str(calc))
                if calc == numbers[i]:
                    valid = True
                    break
                k += 1
            if valid == True:
                break
            j += 1
        if valid == False:
            break
        i += 1
        
    return numbers[i]

#Variables début
preambule = 25

#Ouverture du fichier
file = open("Day9.txt")
#Lecture et copie des données
data = file.read()
#Mise en forme des données
numbers = list(map(int, data.split('\n')))

nb = searchFirstNoSum(preambule, numbers)
            
print(nb)

founded = False

maxi = len(numbers)

#Range de somme
rangeSums = 2
i = 0
j = 0
sumInter = 0
valid = True
foundedMin = 0
foundedMax = 0

# Tant que l'on a pas trouvé et que l'on a pas atteint la limite
while founded == False and rangeSums < maxi:
    i = 0
    for i in range(maxi - rangeSums):
        sumInter = 0
        valid = True
        for j in range(rangeSums):
            sumInter += numbers[i + j]
            if j < rangeSums - 1:
                if sumInter >= nb:
                    valid = False
                    break
        if sumInter != nb:
            valid = False
        if valid:
            foundedMin = i
            foundedMax = i + rangeSums
            founded = True
    rangeSums += 1

print("min : " + str(foundedMin) + " ; max : " + str(foundedMax) + " ; range : " + str(foundedMax - foundedMin))

i = 0

solutions = (numbers[foundedMin:foundedMax]).copy()
print(solutions)
solutions.sort()
print(solutions)
print(solutions[0])
print(solutions[(foundedMax - foundedMin) - 1])
print(solutions[0] + solutions[(foundedMax - foundedMin) - 1])

#Fermeture du fichier
file.close()
