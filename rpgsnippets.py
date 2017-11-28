import random

battle = 1
exp_up = False
level_current = 1
exp_current = 0
exp_max = 4
flee = False
enemy_health = 1
player_health = 1
monster_dead = False

#more than one type of step counter!
'''
#type 1
step = false
step_counter = 10 + random.randint(1,101)
for steps in step_counter:
    if step is True:
        step_counter -= 1
        if step_counter <= 3:
            battle = 0

#type 2
current_step = 0
step_counter = random.randint(1, 101)
for current_step in step_counter:
    if camera_move >= 0:
        current_step +=1
        if current_step >= step_counter:
            battle = 0
    '''#end of step_counters

while battle is 0:
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

    fleeNumberGet = input("Type f to flee")
    if fleeNumberGet.lower() == "f":
        flee_munber = random.randint(1,101)
        if flee_munber <= (33):
            flee = True
            if flee == True:
                battle = 1
                print("You have Fled")
    else:

        if enemy_health == 0:
            battle = 1
            monster_dead = True
        elif player_health == 0:
            game_over = 1

        if monster_dead is True:
            exp_current +=1
            monster_dead = False
        if exp_current >= exp_max:
            exp_up = True
            if exp_up is True:
                level_current +=1
                exp_up = False
            if level_current >= exp_max:
                level_current = 4
        else:
            break

        #dice for stats
one_dee_two = random.randint(1, 3)
one_dee_four = random.randint(1, 5)
one_dee_six = random.randint(1, 7)
one_dee_eight = random.randint(1, 9)
one_dee_ten = random.randint(1, 11)
one_dee_twelve = random.randint(1, 13)
one_dee_twenty = random.randint(1, 21)
one_dee_hundred = random.randint(1, 101)

dice = [one_dee_two, one_dee_four, one_dee_six, one_dee_eight, one_dee_ten, one_dee_twelve, one_dee_twenty, one_dee_hundred]

rando_dice = random.choice(dice)
