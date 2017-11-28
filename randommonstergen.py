import random


battle_start = 1
while battle_start is 1:
    wolf = ('wolf', {'HP': 10, 'MP' : 10})
    bear = ('bear', {'HP': 11, 'MP' : 11})
    hawk = ('hawk', {'HP': 9, 'MP' : 9})
    rat = ('rat', {'HP': 8, 'MP' : 9})
    cobra = ('cobra', {'HP': 12, 'MP' : 9})
    goblin = ('goblin', {'HP': 16, 'MP' : 12})
    giant_rat = ('giant rat', {'HP': 9, 'MP' : 7})
    bugbear = ('bugbear', {'HP': 14, 'MP' : 14})

    monster_names = [wolf, bear, hawk, rat, cobra, goblin, giant_rat, bugbear]

    select = random.choice(monster_names[0:8])
    selectTwo = random.choice(monster_names[0:8]) + random.choice(monster_names[0:8])
    selectThree = random.choice(monster_names[0:8]) + random.choice(monster_names[0:8]) + random.choice(monster_names[0:8])
    selectFour = random.choice(monster_names[0:8]) + random.choice(monster_names[0:8]) + random.choice(monster_names[0:8]) + random.choice(monster_names[0:8])

    selection = [select, selectTwo, selectThree, selectFour]

    selector = random.choice(selection [0:8])

    print (selector)

    battle_start = 0
