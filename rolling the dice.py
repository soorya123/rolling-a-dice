from random import randint
from time import sleep

playerOneWins = 0
playerTwoWins = 0

for i in range(5):
    print("Player 1 it's your turn.         Type 'roll' to roll the dice or 'quit' to forfeit. ")
    userOneInput = input(">>>")
    if userOneInput == "roll":
        valueOne = randint(1, 6)
        print("Player 1 rolled ", valueOne)
        print(" Player 2 it's your turn.         Type 'roll' to roll the dice or 'quit' to forfeit. ")
        userTwoInput = input(">>>")
        if userTwoInput == "roll":
            valueTwo = randint(1, 6)
            print("Player 2 rolled ", valueTwo)
            if valueOne > valueTwo:
                print("Player 1 wins this round! ")
                playerOneWins += 1
            elif valueOne == valueTwo:
                print("It's a draw! ")
            else:
                print("Player 2 wins this round;")
                playerTwoWins += 1
        elif userTwoInput == "quit":
            print("Player 1 wins this round! ")
            playerOneWins += 1
        else:
            print("Program ended abruptly")
            break
    elif userOneInput == "quit":
        print("Player 2 wins this round! ")
        playerTwoWins += 1
    else:
        print("Program ended abruptly. ")
        break

    sleep(2)

print("Final results: ", playerOneWins, "-", playerTwoWins)
if playerOneWins > playerTwoWins:
    print("Player 1 is the winner! ")
elif playerOneWins == playerTwoWins:
    print("It's a draw! ")
else:
    print("Player 2 is the winner! ")