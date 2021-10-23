#Ouverture du fichier
file = open("Day6.txt")
data = file.read()
groups = data.split("\n\n")
questions = {}
totalAll = 0
totalGroup = 0
individuals = ""

for g in groups:
    individuals = g.split('\n')
    questions = {}
    totalGroup = 0
    print("\nGroup : \n" + g + "\n" + "Nombre de personne : " + str(len(individuals)))
    for indi in individuals:
        for c in indi:
            if c not in questions:
                questions[c] = 1
            else:
                questions[c] += 1
    for q in questions:
        print("Question " + str(q) + " : " + str(questions[q]))
        if questions[q] == len(individuals):
            totalGroup += 1
    print("Total group : " + str(totalGroup))
    totalAll += totalGroup
print(totalAll)

#Fermeture du fichier
file.close()
