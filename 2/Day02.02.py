import re
file = open("Day2.txt")
value = 0
for x in file:
    print(x)
    y = re.findall(r"[\w']+", x)
    if bool(y[3][int(y[0]) - 1] == y[2]) ^ bool(y[3][int(y[1]) - 1] == y[2]):
        print(True)
        value = value +1
    else:
        print(False)
print(value)
