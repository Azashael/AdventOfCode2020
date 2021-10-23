import re

#Ouverture du fichier
file = open("Day6.txt")
data = file.read()
groups = data.split("\n\n")
questions = []
total = 0

for g in groups:
    individuals = g.split('\n')
    questions = []
    for indi in individuals:
        for c in indi:
            if c not in questions:
                questions.append(c)
    total += len(questions)

print(total)

#Fermeture du fichier
file.close()
