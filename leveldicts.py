kyloth = {
        "Name" : "Kyloth",
        "Health" : 40,
        "Mana" : 30,
        "Lvl" : 1,
        "Exp" : 0,
        "NextLvl" : 40,
        "strength" : 12,
        "intellect" : 8,
        "agility" : 10,
        "spirit" : 12,
        "accuracy" : 92,
        "dodge" : 18
        }

zire = {
        "Name" : "Zire",
        "Health" : 30,
        "Mana" : 40,
        "Lvl" : 1,
        "Exp" : 0,
        "NextLvl" : 40,
        "strength" : 8,
        "intellect" : 12,
        "agility" : 12,
        "accuracy" : 90,
        "spirit": 10,
        "dodge" : 20
        }



def Level_Up(character):
    while character["Exp"] >= character["NextLvl"]:
        character["Lvl"] += 1
        character["Exp"] = character["Exp"] - character["NextLvl"]
        character["NextLvl"] = round(character["NextLvl"] * 1.37)
        character["Health"] = round(character["Health"] * 1.15)
        character["Mana"] = round(character["Mana"] * 1.15)
        character["strength"] += 1
        character["intellect"] += 1
        character["agility"] += 1
        character["spirit"] += 1
        character["accuracy"] = round(character["accuracy"] * 1.13)
        character["dodge"] = round(character["dodge"] * 1.13)
    print(character["Name"])
    print ("Level: ",  character["Lvl"])
    print ("Exp: ", character["Exp"])
    print ("Next Level: ", character["NextLvl"])
    print("Health: ", character["Health"])
    print("Mana: ", character["Mana"])
    print("Strength: ", character["strength"])
    print ("Intellect: ", character["intellect"])
    print("Agility: ", character["agility"])
    print("Spirit ", character["spirit"])    
    print("Accuracy: ", character["accuracy"])
    print("Dodge: ", character["dodge"])

Level_Up(zire)

print(" ")


zire["Exp"] = 800


Level_Up(zire)

print (" ")

zire["Exp"] = 10000

Level_Up(zire)

print(" ")
print(" ")
print(" ")


print (" ")

zire["Exp"] = 33952

Level_Up(zire)

print(" ")
\


Level_Up(kyloth)

print(" ")


kyloth["Exp"] = 800


Level_Up(kyloth)

print (" ")

kyloth["Exp"] = 10000

Level_Up(kyloth)

print (" ")

kyloth["Exp"] =33952

Level_Up(kyloth)
