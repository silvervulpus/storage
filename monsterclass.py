import random, json

def dice(sides, rolls):
    diceAdded = 0;
    for x in range(rolls):
        diceAdded += random.randint(1, sides)
    return diceAdded



class Monsters:
    def __init__(self, monster_name, HP, MP, movement, accuracy, defense, level, experience, critical_chance, damage, size):

        self.monster_name = monster_name
        self.HP = HP
        self.MP = MP
        self.movement = movement
        self.accuracy = accuracy
        self.defense = defense
        self.level = level
        self.experience = experience
        self.critical_chance = critical_chance
        self.damage = damage
        self.size = size

        if self.size == "small":
            self. HP = HP + 20
            self.MP = MP +20
            self.movement = movement + 4
            self.defense = defense + 4 + dice(6, 2)
            self.accuracy = accuracy + 1 + dice(6, 3)
            self.level = 1
            self.experience = experience + 25
            self.critical_chance = critical_chance + 1
            self. damage = 1 + dice(8, 1)

        if self.size == "medium":
            self. HP = HP + 40
            self.MP = MP +40
            self.movement = movement + 6
            self.defense = defense + 6 + dice(6, 2)
            self.accuracy = accuracy + 6 + dice(6, 4)
            self.level = 2
            self.experience = experience + 75
            self.critical_chance = critical_chance + 3
            self. damage = 1 + dice(12, 1)


        if self.size == "large":
            self. HP = HP + 60
            self.MP = MP +60
            self.movement = movement + 8
            self.defense = defense + 8 + dice(6, 3)
            self.accuracy = accuracy + 8 + dice(6, 6)
            self.level = 4
            self.experience = experience + 100
            self.critical_chance = critical_chance + 6
            self. damage = 1 + dice(20, 1)

        if self.size == "boss":
            self. HP = HP + 80
            self.MP = MP +80
            self.movement = movement + 10
            self.defense = defense + 10 + dice(6, 3)
            self.accuracy = accuracy + 10 + dice(6, 6)
            self.level = 4
            self.experience = experience + 150
            self.critical_chance = critical_chance + 8
            self. damage = 1 + dice(12, 3)


    def stat_return(self):
        monster_dict = {"Class" : self.monster_name,
                    "Health" : self.HP,
                    "Mana" : self.MP,
                    "Move" : self.movement,
                    "Accuracy" : self.accuracy,
                    "Defense" : self.defense,
                    "Level" : self.level,
                    "Exp" : self.experience,
                    "Crit" : self.critical_chance,
                    "Damage" : self.damage,
                    "Size" : self.size}
        print(monster_dict)
        return monster_dict


goblin = Monsters("Goblin", dice(12, 1), dice(12, 1), 1, 1, 1, 1, 0, 10, 1,"small")
orc = Monsters("Orc", dice(20,1), dice(20,1), 2, 2, 2, 2, 0, 14, 1, "medium")
ogre = Monsters("Ogre", dice(12,1) + dice(20, 1), dice(12,1) + dice(20, 1), 4, 4, 4, 4, 0, 16, 1, "large")
giant = Monsters("Giant", dice(10,4), dice(10,4), 6, 6, 6, 6, 0, 18, 1, "boss")

monster_list = [goblin, orc, ogre, giant]

def save_monster():
    print('Writing ...')
    jsondata = []
    for monster in monster_list:
        monsters = monster.stat_return()
        jsondata.append(monsters)
    with open ("monster.json", "w") as monsters:
        monsters.write(json.dumps(jsondata))

save_monster()

def read_monster():
    print('Reading ...')
    with open ("monster.json", "r") as monsters:
        read = json.loads(monsters.read())
        print (read)
        return (read)

read_monster()

"""
print (goblin.stat_return())
print (orc.stat_return())
print (ogre.stat_return())
print (giant.stat_return())
"""