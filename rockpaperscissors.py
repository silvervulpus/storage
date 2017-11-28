import random
from random import randint

rockName = ("Rock")
paperName = ("Paper")
scissorsName = ("Scissors")

rock = 1
paper = 2
scissors = 3
choiceList = [rock, paper, scissors]

wins = 0
losses = 0
ties = 0

def Rounds():
    rounds = input("Choose the number of rounds you wish to play: ")
    rounds = int(rounds)
    if rounds <= 0:
        print("Please select a number greater than 0")
        return Rounds()
    else:
        return int(rounds)

#choiceLoop = False

rounds = Rounds()
i = 1
while i <= rounds :
    i+= 1
    #while choiceLoop is False:
    playerInput =  input("Please Type 1 for Rock, 2 for Paper or 3 for Scissors")
    playerInput = int(playerInput)
    if playerInput is 1:
        print ("you have chosen " + rockName)
    #    choiceLoop = True
    elif playerInput is 2:
        print ("you have chosen " + paperName)
    #    choiceLoop = True
    elif playerInput is 3:
        print ("you have chosen " + scissorsName)
    #    choiceLoop = True
    else:
        print("Invalid selection, please try again!")

    computerChoice = random.randint(1, 3)
    if computerChoice == rock:
        print("The computer chose " + rockName)
    elif computerChoice == paper:
        print ("The computer chose " + paperName)
    elif computerChoice == scissors:
        print ("the computer chose " + scissorsName)


    if computerChoice == playerInput:
        print ("We have a Tie")
        ties += 1
    elif computerChoice == 1 and playerInput == 3:
        print ("Player Loses")
        losses += 1
    elif computerChoice == 2 and playerInput == 1:
        print ("Player Loses")
        losses += 1
    elif computerChoice == 3 and playerInput == 2:
        print ("Player Loses")
        losses += 1
    elif playerInput is 1 and computerChoice == 3:
        print("You Win!")
        wins += 1
    elif playerInput is 2 and computerChoice == 1:
        print("You Win!")
        wins += 1
    elif playerInput is 3 and computerChoice == 2:
        print("You Win!")
        wins += 1
print ("wins", wins, "Losses" , losses,"ties" , ties)
