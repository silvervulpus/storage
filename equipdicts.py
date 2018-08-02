import random
 
critter = random.randrange(1, 99)
 
weapons = {
1: ['short sword',4, 25, 1.5],
2: ['broad sword',6, .25, 1.5],
3: ['long sword',10, .31, 1.5],
}
#name, damage, crit chance,equipped
characters = {
1:['zire', 4, 21, weapons[1]]
}
 
if characters[1][3] == weapons[1]:       characters[1][1] = characters[1][1] + weapons[1][1]
characters[1][2] = characters[1][2] + weapons[1][2]
 
if characters[1][2] >= critter:
    characters[1][1] = characters[1][1] * weapons[1][3]
 
print(critter)
print(characters)
