import random

input("Welcome to ROCK, PAPER, SCISSORS! Press Enter to start. ")

while True:
    uchoice = ["r", "p", "s"]

    cpu = random.choice(uchoice)
    player = None

    while player not in uchoice:
        player = input("R for Rock, P for Paper, S for Scissors. Choose\n").lower()
        while uchoice != "r" and uchoice != "p" and uchoice != "s":
            uchoice = input("Invalid input, please try again: ")
    if player == cpu:
        print("CPU: ",cpu)
        print("Player: ",player)
        print("Its a tie!")
    elif player == "r":
        if cpu == "p":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You lose!")
        if cpu == "s":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You win!")
    elif player == "p":
        if cpu == "s":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You lose!")
        if cpu == "rock":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You win!")
    elif player == "s":
        if cpu == "r":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You lose!")
        if cpu == "p":
            print("CPU: ",cpu)
            print("Player: ",player)
            print("You win!")

    play_again = input("Play Again? (YES/NO): ").lower()
    while play_again != "yes" and play_again != "no":
            play_again = input("Invalid input, please try again").lower()
    if play_again != "yes":
        break
print("BYE! Come again^-^")
    


