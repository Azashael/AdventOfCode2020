import re

def numbersBags(bagsRules, colorName, bagsAlreadyFounded : set):
    for b in bagsRules:
        if colorName in bagsRules[b]:
            bagsAlreadyFounded = bagsAlreadyFounded.union(numbersBags(bagsRules, b, bagsAlreadyFounded))
            bagsAlreadyFounded.add(b)
    return bagsAlreadyFounded

# Regex
# Pour la 1e partie, les sacs contenants
# (.*)(?= bags contain)
# Pour la 2e partie, les sacs contenus
# (?<= bags contain )(.*)
# Pour split la 2e partie en plusieurs sacs
# \d+ (.*?)(?= bag.| bags.| bag,| bags,)|no other bags
# Pour récupèrer le nombre
# \d+
# Pour récupèrer la couleur
# (?<=\d ).*

#Ouverture du fichier
file = open("Day7.txt")
#Lecture et copie des données
data = file.read()

rules = data.split('\n')
rulesDict = {}
ruleBags = []
colorName = ""
colorNameWanted = input()

for r in rules:
    ruleBags = []
    colorName = (re.search("(.*)(?= bags contain)", r)).group()
    ruleBags = re.findall("(?<=\d )(.*?)(?= bag.| bags.| bag,| bags,)",r)
    if colorName not in rulesDict:
        rulesDict[colorName] = ruleBags

print(rulesDict)

bagsSet = set()
bagsSet = numbersBags(rulesDict, colorNameWanted, bagsSet)

print(len(bagsSet))
#Fermeture du fichier
file.close()
