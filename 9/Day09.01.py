#Variables début
preambule = 25

#Ouverture du fichier
file = open("Day9.txt")
#Lecture et copie des données
data = file.read()
#Mise en forme des données
numbers = list(map(int, data.split('\n')))

i = preambule
l = preambule
j = 0
k = 0
maxi = len(numbers)
valid = False
calc = 0
print(numbers)

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
            
print(i)
print(numbers[i])

#Fermeture du fichier
file.close()
