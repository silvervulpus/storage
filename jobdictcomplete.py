import random, json

def dice(sides, rolls):
    diceAdded = 0;
    for x in range(rolls):
        diceAdded += random.randint(1, sides)
    return diceAdded

class Jobs:
    def __init__(self,job_name, HP, MP, movement, accuracy, defense, level, experience, critical_chance, damage):
        self.job_name = job_name
        self.HP = HP + dice(10, 1)
        self.MP = MP + dice(10, 1)
        self.movement = movement + 1
        self.accuracy = accuracy + 6 + dice(6, 3)
        self.defense = defense + 6 +   dice(6, 2)
        self.level = level
        self.experience = experience
        self.critical_chance = critical_chance + 5
        self.damage = damage

    def stat_return(self, jobs):
        job_dict = {"Class" : self.job_name,
                    "Health" : self.HP,
                    "Mana" : self.MP,
                    "Move" : self.movement,
                    "Accuracy" : self.accuracy,
                    "Defense" : self.defense,
                    "Level" : self.level,
                    "Exp" : self.experience,
                    "Crit" : self.critical_chance,
                    "Damage" : self.damage}
        print(job_dict)
        return job_dict, jobs

fighter = Jobs("Fighter", 30, 10, 6, 2, 1, 1, 0, 2, 1)
rogue = Jobs("Rogue", 20, 20, 7, 3, 0, 1, 0, 3, 1)
wizard = Jobs("Wizard",15 ,30 , 6, 2, 1, 1, 0, 1, 1)
cleric = Jobs("Cleric",25 ,20 , 6, 1, 2, 1, 0, 1, 1)
ranger = Jobs("Ranger", 20, 20, 7, 3, 0, 1, 0, 2, 1)
monk = Jobs("Monk", 25, 15, 7, 2, 1, 1, 0, 3, 1)
paladin = Jobs("Paladin", 30, 15, 6, 1, 2, 1, 0, 1, 1)
bard = Jobs("Bard", 25, 25, 6, 1, 2, 1, 0, 3, 1)
alchemist = Jobs("Alchemist", 15, 25, 7, 2, 1, 1, 0,2, 1)
afflictionist = Jobs("Afflictionist", 20, 25, 7, 3, 0, 1, 0,2, 1)
gunner = Jobs("Gunner", 20, 20, 6, 2, 1, 1, 0,3, 1)
druid = Jobs("Druid", 25, 20, 7, 2, 1, 1, 0,2, 1)
mimic = Jobs("Mimic", 20, 20, 6, 2, 1, 1, 0, 1, 1)


joblist = [fighter,rogue,wizard,cleric,ranger,monk,paladin,bard,alchemist,afflictionist,gunner,druid,mimic]
#print("fighter 1,\nrogue 2,\nwizard, 3\ncleric 4,\nranger 5,\nmonk, 6\npaladin 7,\nbard 8,\nalchemist 9,\nafflictionist 10,\ngunner 11,\ndruid 12,\nmimic 13")

#job_pick = input("Please type the name or number of the job you wish to play from this list: ")

#for job in joblist:
    #print(job.stat_return(joblist))





def save_stats():
    print('Writing ...')
    jsondata = []
    for job in joblist:
        stats, jobbie = job.stat_return(job)
        jsondata.append(stats)
    with open ("stats.json", "w") as stats:
        stats.write(json.dumps(jsondata))

save_stats()

def read_stats():
    print('Reading ...')
    with open ("stats.json", "r") as stats:
        read = json.loads(stats.read())
        print (read)
        return read

read_stats()



