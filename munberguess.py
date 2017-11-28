import random
compMunber = random.randint(1,101)
print("Can you guess what number i am thinking of? You may have 10 guesses.")
for i in range(10):
    playerInput = int(input("Please enter the number you are guessing "))
    if playerInput == compMunber:
        print("That is correct you win!")
        break
    elif playerInput > compMunber:
        print ("Your Guess is too High!")
    elif playerInput < compMunber:
        print ("Your Guess is too Low")
    else:
        print("Invalid selection ")
