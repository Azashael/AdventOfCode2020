#import regex
import re

def tryChange(actions):
    i = 0
    maxi = len(actions)
    codeAction = ""
    valueAcc = 0
    negpos = ""
    digit = 0
    listi = []

    while i < maxi:
        if i in listi:
            return 0
        listi.append(i)
        codeAction = (re.search("^[a-z]{3}", actions[i])).group()
        if codeAction == "nop":
            i += 1
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
            if negpos == "+":
                i += digit
            elif negpos == "-":
                i -= digit
        else :
            i += 1
    return valueAcc

#Ouverture du fichier
file = open("Day8.txt")
#Lecture et copie des données
data = file.read()

actions = data.split('\n')
actionsDouble = actions.copy()

i = 0
maxi = len(actions)
accValue = 0

print(actions)

while i < maxi:
    actionsDouble = actions.copy()
    codeAction = (re.search("^[a-z]{3}", actions[i])).group()
    if codeAction == "nop":
        actionsDouble[i] = re.sub("nop", "jmp", actions[i])
    elif codeAction == "jmp":
        actionsDouble[i] = re.sub("jmp", "nop", actions[i])
    accValue = tryChange(actionsDouble)
    if accValue > 0:
        break
    i += 1

print(accValue)

#Fermeture du fichier
file.close()
