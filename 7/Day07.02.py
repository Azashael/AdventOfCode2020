import re

def numbersBags(bagsRules, colorName) -> int:
    nb = 0
    #print(colorName)
    #print(bagsRules[colorName])
    if bagsRules[colorName]:
        for b in bagsRules[colorName]:
            #print(b)
            nb += b[0] + b[0] * numbersBags(bagsRules, b[1])
        return nb
    else:
        return nb

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
tempColorName = ""
tempNbBags = 0

for r in rules:
    ruleBags = []
    colorName = (re.search("(.*)(?= bags contain)", r)).group()
    ruleBags = re.findall("(\d+ .*?)(?= bag.| bags.| bag,| bags,)",r)
    if colorName not in rulesDict:
        rulesDict[colorName] = list()
        for part in ruleBags:
            rulesDict[colorName].append(tuple((int((re.search("\d+", part)).group()), (re.search('(?<=\d )(.*)', part)).group())))

#print(rulesDict)

bagsSet = 0
bagsSet = numbersBags(rulesDict, colorNameWanted)

print(bagsSet)
#Fermeture du fichier
file.close()
