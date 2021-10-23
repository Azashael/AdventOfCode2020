#import regex
import re

#Ouverture du fichier
file = open("Day8.txt")
#Lecture et copie des données
data = file.read()

actions = data.split('\n')
i = 0
maxi = len(actions)
codeAction = ""
valueAcc = 0
negpos = ""
digit = 0
listi = []
countJmp = 0
countNop = 0

while i < maxi:
    if i in listi:
        break
    listi.append(i)
    codeAction = (re.search("^[a-z]{3}", actions[i])).group()
    if codeAction == "nop":
        i += 1
        countNop += 1
        continue
    negpos = (re.search("[+-]", actions[i])).group()
    digit = int((re.search("[0-9]+", actions[i])).group())
    if codeAction == "acc":
        if negpos == "+":
            valueAcc += digit
        elif negpos == "-":
            valueAcc -= digit
        i += 1
    elif codeAction == "jmp":
        countJmp += 1
        if negpos == "+":
            i += digit
        elif negpos == "-":
            i -= digit
    else :
        i += 1

print(valueAcc)
print(countJmp)
print(countNop)

#Fermeture du fichier
file.close()
