def treeSeeker(grid, rc, dc):
    r = 0
    d = 0
    value = 0
    while d < len(grid):
        if grid[d][r % len(grid[d])] == '#':
            value += 1
        r += rc
        d += dc
    return value

#Ouverture du fichier
file = open("Day3.txt")
grid = file.read().splitlines()
#Réponse
value = 1

tabTest = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for tup in tabTest:
    value *= treeSeeker(grid, tup[0], tup[1])
    
print(value)
#Fermeture du fichier
file.close()


        
