"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""

import re
#Ouverture du fichier
file = open("Day4.txt")
passportsFiles = file.read()
passportsFilesSplit = passportsFiles.split("\n\n")
value = 0
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

for p in passportsFilesSplit:
    p = p.replace('\n', ' ')
    q = p.split(' ')
    if len(q) < 7:
        continue       
    else:
        groups = re.findall('(\w+):([\w#]+)', p)
        line = dict(groups)
        if not(set(fields) <= set(line)):
            continue
        if int(line["byr"]) < 1920 or int(line["byr"]) > 2002:
            continue
        if int(line["iyr"]) < 2010 or int(line["iyr"]) > 2020:
            continue
        if int(line["eyr"]) < 2020 or int(line["eyr"]) > 2030:
            continue
        if not(re.search("^#(([\da-fA-F]{3}){2}|([\da-fA-F]{4}){2})$", line["hcl"])):
            continue
        if not(re.search("(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)", line["ecl"])):
            continue
        if not(re.search("(^(19[0-3]|1[5-9][0-9])cm$|^(6[0-9]|7[0-6]|59)in$)", line["hgt"])):
            continue
        if not(re.search("^[0-9]{9}$", line["pid"])):
            continue
        print(p)
    value += 1
print(value)

#Fermeture du fichier
file.close()
