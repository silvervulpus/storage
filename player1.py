import pygame
import shelve
import time
import random
import datetime
import math
import sys
from time import sleep
from random import randint
from datetime import datetime
from math import pi
now = datetime.now()
print (now)
pygame.init()

sleep (1)

#Player 1 Account Name
accoName = input("Please choose a Name for your Account: ")
print ("nice to meet you " + accoName[0].upper() + accoName[1:].lower())

#Player 1 Account Password
passVerify = 0
while passVerify <=0:
    accoPass = input("Please choose a Password: ")
    accoPassVerify = input("Please type the Password again: ")
    accoPass = accoPass.lower()
    accoPassVerify = accoPassVerify.lower()
    if accoPass == accoPassVerify:
        print ("Your password is set to be: " + accoPassVerify)
        passVerify = 1
    else:
        print("your passwords do not match. we will send a new number. please try again")
#player 1 Account Email
accoEmail = input("Please enter a valid email: ")

#player 1 Account verify number
sleep (1.5)

emailVerify = 0
while emailVerify <= 0:
    print ("A Number has been Emailed to you at "+ accoEmail)
    makeVerNum = random.randint(1001,1990)
    dudePi = pi // 1
    makeVerNum = makeVerNum + dudePi
    makeVerNum = int(makeVerNum)
    print (makeVerNum)
    verifyNumReturn = int(input("Please enter the number from your Email: "))
   # verifyNumReturn = int(verifyNumReturn)
    if verifyNumReturn == makeVerNum:
        emailVerify = 1
        print("Enjoy the game!")
    else:
        print("the number is invalid, cannot verify account.")

sleep (1.5)


#Player 1 Toon Name
toonName = input("Please enter a Name for your Toon: ")
print (toonName[0].upper()+toonName[1:].lower())

#Player 1 Gender
gender = 0
while gender <= 0:
    toonSex = input("Please tell us if you are a Man or a Woman. Type M for Man and W for Woman. ")
    if toonSex.lower() == "m" or toonSex.lower() == "man":
        print ("you have chosen to be male")
        gender = 1

    elif toonSex.lower() == "w" or toonSex.lower() == "woman":
        print ("you have chosen to be female.")
        gender = 2
    elif toonSex.lower() == "apache attack helicoper" or toonSex.lower() == "apacheattackhelicopter" or toonSex.lower() == "aah":
        print ("oh really? me too!!!!")
        gender = 3
    else:
        print(" i sexually identify as an apache attack helicopter. but i am  still a guy, try again!")
#Player 1 Class
classChoice = 0
while classChoice <= 0:
    classChoiceInput = input("would you like to play a fighter, a rogue,  or a mage?")
    if classChoiceInput.lower() == "fighter":
        print("You wish to play a fighter!")
        classChoice = 1
    elif classChoiceInput.lower() == "rogue":
        print("you wish to play a rogue!")
        classChoice = 2
    elif classChoiceInput.lower() == "mage":
        print("you wish to play a mage!")
        classChoice = 3
    else:
        print("well isn\'t it exciting, how about one from the list?")

print("what would you like your weapon to be?")

#weapon selection
charweapon = 0
while charweapon <= 0:
    maincharweapon = input("What do you choose to weild?\nSword? Staff? Shield?")

    if maincharweapon.lower() == "sword":
        print("Valiant Warrior, you have choosen the Blade!")
        charweapon = 1
    elif maincharweapon.lower() == "staff":
        print("Wise Adventurer, You have choosen the Sceptre!")
        charweapon = 2
    elif maincharweapon.lower() == "sheild":
        print("Bold Defender, you have choosen the Bulwark!")
        charweapon = 3
    else:
        print("Whaddaya want from us? a gun?!?")

#Dictionary of items
def shelve(inventory, item_list):
    for p in item_list:
        if p[0] in inventory:
            try:
                inventory[p[0]] += p[1]
                if inventory[p[0]] < 0:
                    raise ValueError('negative amount for product')
            except ValueError as ve:
                print(ve)
                inventory[p[0]] -= p[1]
        else:
            inventory[p[0]] = p[1]
    print(inventory)
weapList = {"sword":1, "dagger":2, "round shield":3}
armourItems = [("boots",4),("potion",-1),("tunic",6)]

shelve(weapList, armourItems)
shelve(weapList,[("sword",-1000)])


#string substitution
#str substitution
storyFormat = '''
So one day theres this {person} right? aaand this {person} love to eat {food}.
and the {person} was broke in the {hood}. ya see {the_man} was
keeping the {person} down. so the {person} wanted to escape the {hood} and
get back to the{wild} where he was free of {the_man}.
'''

def tellStory ():
    userPicks = dict()
    addPick('person' , userPicks)
    addPick('the_man' , userPicks)
    addPick('hood' , userPicks)
    addPick('wild' , userPicks)
    addPick('food' , userPicks)
    story = storyFormat.format(**userPicks)
    print (story)

def addPick(cue, dictionary):
    prompt = 'enter an example for ' + cue +': '
    response = input(prompt)
    dictionary[cue] = response
tellStory()
input('Press Enter to end the program')




#Player 1 Experience Current
expCurr = 1
#Player 1 Experience Full
expFull = 100 #increase by 25.8 + pi per lvl
#player 1 Experience Needed For Max Level
expMax = 10000

#Player 1 Health
hpCurr = 1
#player 1 Health Full
hpFull = 100
#Player 1 Mana
mpCurr = 1
#Player 1 Mana Full
mpFull = 100
#Player 1 Armor
armorBase = 1
#Player 1 Magic Resistance
mrBase = 1
#Player 1 Dodge
dodgeBase = 1
#Player 1 Accuracy
accuracyBase = 1
#player 1 Attack Damage
atkBase = 1
#Player 1 Magic Damage
magBase = 1
#player 1 Critical Magic Damage
critMagDmg = 1
#player 1 Critical Attack Damage
critAtkDmg = 1
#player 1 Critical Chance
critChance = 1
#Player 1 Class Stat Modifier
fightStatMod = (1 + atkBase)
rogueStatmod = (1 + dodgeBase)
mageStatMod = (1 + magBase)

#player 1 Movement
movement = 1


#Weapons may be one or two handed and offer an extra effect or ability upon use

#weapon modifiers define weapon name and stats
#class Weapons:
 #   def weapons(self, name, buy, sell, physDam, magDam, accuracy, criticalChance, criticalBonus, armor, dodge, magResist, movement, reach, handed, mainOff, equipped, unequipped):


#player 1 Weapon Name
#player 1 Weapon Cost Buy
#player 1 Weapon Cost Sell
#player 1 Attack Damage Modifier
#player 1 Magic Damage Modifier
#player 1 Accuracy Modifier
#player 1 Critical Chance Modifier
#player 1 Critical Attack Damage Modifier
#player 1 Critical Magic Damage Modifier
#player 1 Weapon Range
#player 1 One or Two Handed
#player 1 Main or Off Hand
#player 1 Weapons Special Effects

#Shields may be a Weapon or an Armor, and 1 or 2 handed When a two handed Shield is equipped as an Armor, it takes the Cape slot
#When a shield is one handed it can be equipped to the main or offhand slot
#if a shield is equipped to the main or off or both hand slots, it may be used as a weapon.
#'''

#Holding a weapon in the offhand offers an Armor/M.R./Dodge Modifier, even if it isnt a shield.

#Armor in Light, which offers the most Magic Resist and the least Armor
#Or in Medium, Which offers the most Dodge and the least Magic Resist,
#Or in Heavy, which offers the most Armor and the least Dodge

#player 1 Armor Name
#player 1 Armor Cost Buy
#player 1 Armor Cost Sell
#player 1 Armor Type (Light, Medium, Heavy)
#player 1 Bonus Armor Modifier
#player 1 Magic Resistance Modifier
#player 1 Dodge Modifier
#player 1 Armor Special Effects
#player 1 Armor Slot Used
#Head, Chest, Legs, Belt, Boots, Gloves, Shield, Neck, Ring, Wrist, Cape, Quiver.

#''' Ammo and Quivers have their own stat modifiers seperate from regular armor or weapon stats.
#Ammo effects all damage based stats. Ammo Capacity is dependant on the Quiver.
#Quivers do not effect critical damage. only base damages.
#Quivers are always light armor. Quivers effect only some Damage stats and all Armor stats
#Quivers Replace the Belt or Cape Armor slot.'''

#player 1 Ammo Type
#player 1 Ammo Name
#player 1 Ammo Cost Buy
#player 1 Ammo Cost Sell
#player 1 Ammo Attack Damage Modifier
#player 1 Ammo Magic Damage Modifier
#player 1 Ammo Critical Chance Modifier
#player 1 Ammo Critical Magic Damage Modifier
#player 1 Ammo Critical Attack Damage Modifier
#player 1 Ammo Accuracy Modifier
#player 1 Ammo Special Effects


#player 1 Quiver Name
#player 1 Quiver Cost Buy
#player 1 Quiver Cost Sell
#player 1 Quiver Capacity Full
#player 1 Quiver Capacity Current
#player 1 Quiver Attack Damage Modifier
#player 1 Quiver Magic Damage Modifier
#player 1 Quiver Critical Chance Modifier
#player 1 Quiver Armor Modifier
#player 1 Quiver Magic Resist Modifier
#player 1 Quiver Dodge Modifier
#player 1 Quiver Accuracy Modifier
#player 1 Quiver Special Effects
total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total += new_number
print("The total is: ", total)
print("Done.")
print("If you can count to 15 in three\'s, this game is over.")
for i in range (0,16,3):
   print(i)
