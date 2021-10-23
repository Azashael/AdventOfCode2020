import math
#Ouverture du fichier
file = open("Day5.txt")
passes = file.read()
passesSplit = passes.split("\n")
valueMax = 0
valueMin = 127 * 8 + 7
passeslist = []

minRow = 0
maxRow = 127
minCol = 0
maxCol = 7
interRow = 0
interCol = 0
i = 0
passId = 0

for p in passesSplit:
    minRow = 0
    maxRow = 127
    minCol = 0
    maxCol = 7
    interRow = 0
    interCol = 0
    i = 0
    while i < 10:
        if( i < 7 ):
            interRow = minRow + ((maxRow - minRow) / 2)
            if p[i] == 'F':
                maxRow = math.floor(interRow)
            elif p[i] == 'B':
                minRow = math.ceil(interRow)
        else:
            interCol = minCol + ((maxCol - minCol) / 2)
            if p[i] == 'L':
                maxCol = math.floor(interCol)
            elif p[i] == 'R':
                minCol = math.ceil(interCol)
        i += 1
    passId = minRow * 8 + minCol
    passeslist.append(passId)
    if passId > valueMax:
        valueMax = passId
    if passId < valueMin:
        valueMin = passId
    #print("Pass : " + p + " ; Row : " + str(minRow) + " ; Col : " + str(minCol) + " ; Id : " + str(passId) + " ; Highest : " + str(valueMax) + " ; Smallest : " + str(valueMin))

passeslist.sort()
lenPasses = len(passeslist)
i = 1
cal = 0
while i < lenPasses:
    cal = passeslist[i] - passeslist[i - 1]
    if cal > 1:
        print (passeslist[i] - 1)
        break
    i += 1

#Fermeture du fichier
file.close()
