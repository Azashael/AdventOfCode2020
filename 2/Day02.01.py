import re
file = open("Day2.txt")
value = 0
for x in file:
    print(x)
    y = re.findall(r"[\w']+", x)
    if y[3].count(y[2]) >= int(y[0]) and y[3].count(y[2]) <= int(y[1]):
        print(True)
        value = value + 1
    else:
        print(False)
print(value)
