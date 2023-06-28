# This program is a number guessing program
import random

logo='''                                                                                     

.------..------..------..------..------..------.     .------..------..------..------..------.     .------..------..------..------.
|N.--. ||U.--. ||M.--. ||B.--. ||E.--. ||R.--. |.-.  |G.--. ||U.--. ||E.--. ||S.--. ||S.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :(): || (\/) || (\/) || :(): || (\/) || :(): ((5)) | :/\: || (\/) || (\/) || :/\: || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
| ()() || :\/: || :\/: || ()() || :\/: || ()() |'-.-.| :\/: || :\/: || :\/: || :\/: || :\/: |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'N|| '--'U|| '--'M|| '--'B|| '--'E|| '--'R| ((1)) '--'G|| '--'U|| '--'E|| '--'S|| '--'S| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'

'''
logo.__sizeof__()
computer_guess = 0
turns = 0
end_of_program = False


def computer():
    global computer_guess
    computer_guess = random.randint(1, 100)


def easy():
    global turns
    turns = 10


def hard():
    global turns
    truns = 5


while end_of_program == False:
    print(logo)
    print("Welcome to the number guesing game.")
    print("I am thinking of a number between 1 and 100.")
    computer()

    difficulty = input("please choose a difficulty level:\n1.Easy\n2.Hard\n--->")
    if difficulty == "easy" or "Easy":
        easy()
        while turns > 0:
            guess = int(input("Make a guess:\n--->"))
            if guess == computer_guess:
                print("YAY!!! YOU GUESSED IT RIGHT!!!")
                break

            elif guess < computer_guess:
                print("Wrong!!! Guess Higher.")
                turns -= 1
                print(f"Turns remaining:{turns}")
                if turns == 0:
                    print("YOU ARE OUT OF TURNS. YOU LOST!!!")
            elif guess > computer_guess:
                print("Wrong!!! Guess Lower.")
                turns -= 1
                print(f"Turns remaining:{turns}")
                if turns == 0:
                    print("YOU ARE OUT OF TURNS. YOU LOST!!!")

    elif difficulty == "hard" or "Hard":
        hard()
        while turns > 0:
            guess = int(input("Make a guess:\n--->"))
            if guess == computer_guess:
                print("YAY!!! YOU GUESSED IT RIGHT!!!")
            elif guess < computer_guess:
                print("Wrong!!! Guess Higher.")
                turns -= 1
                print(f"Turns remaining:{turns}")
                if turns == 0:
                    print("YOU ARE OUT OF TURNS. YOU LOST!!!")
            elif guess > computer_guess:
                print("Wrong!!! Guess Lower.")
                turns -= 1
                print(f"Turns remaining:{turns}")
                if turns == 0:
                    print("YOU ARE OUT OF TURNS. YOU LOST!!!")
    else:
        print("Choose a valid command")
        continue
