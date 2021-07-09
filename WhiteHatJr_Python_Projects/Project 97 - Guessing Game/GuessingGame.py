import random
import time
import os

chances = 0
fakeChances = 5
r = None
stopGame = False
EASY = 10
MEDIUM = 100
HARD = 500

def clear_screen():
    os.system("cls")

def Win():
    global stopGame
    global chances
    global fakeChances

    playAgainInput = input("Do you want to play again.(Y/N)").upper()
    if playAgainInput == "Y":
        fakeChances = 5
        chances = 0
        clear_screen()
        main()

    else:
        clear_screen()
        stopGame = True

def Lose():
    global chances
    global stopGame
    global fakeChances

    print("\nYou Lose!\nThe Number was", r, ".")
    time.sleep(1)
    playAgainInput = input("Do you want to play again.(Y/N)").upper()
    if playAgainInput == "Y":
        fakeChances = 5
        chances = 0
        clear_screen()
        main()

    else:
        clear_screen()
        stopGame = True

class bcolors:
    GREEN = "\033[1;32;92m"
    YELLOW = "\033[1;4;93m"
    RED = "\033[1;24;91m"
    RESET = "\033[1;32;0m"
    BOLD = "\033[1m"


def main():
    global stopGame
    global chances
    global fakeChances
    global r
    global EASY
    global MEDIUM
    global HARD

    clear_screen()
    time.sleep(1)
    print(f"{bcolors.YELLOW}Welcome to Guess the Number!{bcolors.RESET}")
    time.sleep(1)
    print(bcolors.RED + "You have", fakeChances, "chances!" + bcolors.RESET)
    time.sleep(0.5)
    print(f"{bcolors.BOLD}EASY = 1 to 10")
    time.sleep(0.25)
    print("MEDIUM = 1 to 100")
    time.sleep(0.25)
    print(f"HARD = 1 to 500{bcolors.RESET}")
    time.sleep(0.5)
    playerInput = input(f"{bcolors.GREEN}Please Enter Your Difficulty(EASY/MEDIUM/HARD){bcolors.RESET}\n").upper()
    print(bcolors.BOLD + "You Chose the Difficulty as " + playerInput + "." + bcolors.RESET)
    if (playerInput == "EASY"):
        r = random.randrange(1, 10)
    elif (playerInput == "MEDIUM"):
        r = random.randrange(1, 100)
    elif (playerInput == "HARD"):
        r = random.randrange(1, 500)
    time.sleep(1)

    while chances < 5:

        playerInput = input(f"{bcolors.GREEN}Please Guess Your Number{bcolors.RESET}\n")

        if playerInput == "":
            print("Please Type a Number!")
            time.sleep(1)

        elif playerInput.isalpha():
            print("Please Type a Number!")
            time.sleep(1)

        elif int(playerInput) == r:
            print("You Win!")
            Win()
            break

        elif int(playerInput) > r:
            fakeChances -= 1
            print("The number is smaller than the number you guessed.\nYou have", fakeChances, "left.")
            chances += 1

        elif int(playerInput) < r:
            fakeChances -= 1
            print("The number is greater than the number you guessed.\nYou have", fakeChances, "left.")
            chances += 1

        if stopGame == True:
            break

        if not chances < 5:
            Lose()

main()

