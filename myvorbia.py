import random, time, sys
from time import sleep


global decisions
decisions = 0


print("""Welcome to Myvorbia! We are happy to see you here, small creature!
We adore your kind, small creature, but we cant keep calling you that...
We must find a new name.... I have an idea!""")

def My_Name():#decisions?
    global decisions
    global name
    sleep (0.5)
    name = input("May we ask your name? ")
    age = input("May we ask how old you are? ")
    sleep(0.7)
    print ("Hmm, " + name + " are you sure you want me to call you that?")
    looper = 0
    while looper == 0:
        new = input("If you want us to keep your name, say yes. If not, say no! ")
        new = new.lower()

        if new == "yes":
            looper = 1
            sleep(0.7)
            decisions += 4
            print(decisions)
            pass
        elif new == "no":
            name = input("What should we name you then? ")
            decisions += 1
            sleep(0.5)
            print ("Ahh, " + name + " That is very nice. We like that!")
            print (decisions)
            looper = 2
            return name

        elif new == "exit":
            sys.exit()

        else:
            looper = 0


def Fun_Game():
    sleep(0.7)
    storyline =  "Ok " +  name + '''
    We have decided what game we want to play
    with you. We decided we wanted you to play "Be Lost".
    Would you like to play?
    If you do not want to play with us.
    You may exit the game by entering "exit" at any destination.
    But for now, Good bye!
    '''
    print (storyline)

def Laughable_Beginning():
    global decisions
    storyline1 ="""
    You are standing in a forested valley.
    the dirt rises in high mounds to either side of you, carrying with it,
    the gnarled roots, too thick to pass.
    the leaves and grasses around you glow soft silvers,
    reds and purples in the moonlight.
    Shadows dance across the leaves, in and out of the wind.
    There is a dirt path running beneath you.
    you must choose left or right.
    """
    print (storyline1)
    sleep(0.7)
    story_decide_1 = input("left or right? ")
    story_decide_1 = story_decide_1.lower()
    if story_decide_1 == "left":
        decisions += 3
        print(decisions)
        sleep(0.7)
        next_function1()
    elif story_decide_1 == "right":
        sleep(0.7)
        next_function2()
        decisions += 2
        print(decisions)
    elif story_decide_1 == "exit":
        sys.exit()
    elif story_decide_1 != "left" or story_decide_1 != "right" or story_decide_1 != "exit":
        sleep(0.7)
        Laughable_Beginning()

def next_function1():
    global decisions
    forest_left = """
    The forest begins to grow dense around you.
    As you walk down the dirt path, the light recedes behind the
    thickening branches and boughs above you.
    A strange feeling of comfort seems to wash over you,
    as you come to a small, dark glade.
    The sound of water is faint in the distance.
    as the path leads forward you find vines and thorns become walls around you.
    The coils and spindles begin to lower.
    you find yourself having to crouch and crawl at places.
    As you come to a small hole in the ground,
    you peek and see a ladder leading down it.

    """
    print (forest_left)
    thorny = input("do you choose to move forward, back or down? ")
    thorny = thorny.lower()
    if thorny == "down":
        tunnel()
        decisions +=2
        sleep(0.7)
    elif thorny == "forward":
        thorny_walls()
        decisions +=2
        sleep(0.7)
    elif thorny == "back":
        decisions -=1
        sleep(0.7)
        Laughable_Beginning()
    elif thorny == "exit":
        sys.exit()

    elif thorny != "down" or thorny != "forward" or thorny != "back" or thorny != "exit":
        sleep(0.7)
        next_function1()



def next_function2():
    global location
    location = "forest"
    global decisions
    forest_right = """ The forested path begins to climb at a steep rate.
    The rocks and gravel become shifting beneath your feet.
    Through the sliding and the extra steps, you come to a flat rock jutting
    from the side of mountain. as you achieve the flat, you turn and
    see a vast forest below you. the clouds are thick on the horizons.
    You cannot see very far into the dense fog, as it falls onto the forest.
    but you do notice a small waterfall not far from where you started.
    the moonlight makes the forest give off a faint silver and purple glow
    below you. From the rock flat, there is visible, a footpath carved
    into the face of the mountain, leading around the mountainside.
    above you, there is a cave with a faint glow of fire coming from inside.
    you begin to feel how cold the muggy night is on your skin.
    """
    print (forest_right)
    flat = input("Would you like to go up, back, or around? ")
    flat = flat.lower()
    if flat == "around":
        decisions +=2
        sleep(0.7)
        mountain_face()
        decisions += 3
    elif flat == "up":
        sleep(0.7)
        mountain_cave()
    elif flat == "back":
        decisions -= 1
        sleep(0.7)
        Laughable_Beginning()
    elif flat == "exit":
        sys.exit()
    elif flat != "up" or flat != "around" or flat != "back" or flat != "exit":
        next_function2()

def thorny_walls():
    thornywalls = """ placeholder for thorny crawl story"""
    print (thornywalls)


def tunnel():
    tunnel = """placeholder for tunnel story """
    print (tunnel)

def waterfall():
    waterfall_story = """place holder for waterfall """

def mountain_face():
    cliffside = """cliff on ledge from flat"""
    print(cliffside)

def mountain_cave():
    cave = """cave with fire"""


My_Name()#decisions
Fun_Game()
Laughable_Beginning()
