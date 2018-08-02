import random

new_character = {

}

def New_Character(new_character):
    names =["John","Carol","Sherry","Zeke","Bill","Tara" ]
    namer = random.choice(names)
    hp_gen = random.randint(25, 45)
    mp_gen = random.randint(25, 45)
    strength_gen = random.randint(8, 14)
    intellect_gen = random.randint(8, 14)
    agility_gen = random.randint(8, 14)
    accuracy_gen = random.randint(85, 94)
    dodge_gen = random.randint(16, 24)


    new_character = {
        "Name" : "{}".format(namer),
        "Health" : "{}".format(hp_gen),
        "Mana" : "{}".format(mp_gen),
        "Lvl" : 1,
        "Exp" : 0,
        "NextLvl" : 40,
        "str" : "{}".format(strength_gen),
        "int" : "{}".format(intellect_gen),
        "agi" : "{}".format(agility_gen),
        "accuracy" : "{}".format(accuracy_gen),
        "dodge" : "{}".format(dodge_gen )

}
    print(" ")
    print(new_character["Name"])
    print ("Level: ",  new_character["Lvl"])
    print ("Exp: ", new_character["Exp"])
    print ("Next Level: ", new_character["NextLvl"])
    print("Health: ", new_character["Health"])
    print("Mana: ", new_character["Mana"])
    print("Strength: ", new_character["str"])
    print ("Intellect: ", new_character["int"])
    print("Agility: ", new_character["agi"])
    print("Accuracy: ", new_character["accuracy"])
    print("Dodge: ", new_character["dodge"])
    print(" ")


New_Character(new_character)

New_Character(new_character)

New_Character(new_character)