# A BlackJack game
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
]
comp = []
user = []
end_of_game = False
end_of_game2=False


def computer():
    global cards
    global comp
    comp = random.choices(cards, k=2)
    print(comp[0])
    return comp


def player():
    global cards
    global user
    user = random.choices(cards, k=2)
    print(f"Your cards:{user}, current score:{sum(user)}")
    return user


while end_of_game == False:
    start = input(
        "Do you want to start the game?.\nType 'y' for YES and 'no' for NO.\n---->"
    )
    if start == "y":
        player()
        computer()
        while end_of_game2==False:
            turn = input("Type 'y' to get another card and 'n' to pass.")
            if turn == "y":
                x = random.choice(cards)
                y = random.choice(cards)
                user.append(x)
                comp.append(y)
                print(f"your cards:{user},current score:{sum(user)}")
                print(f"computer's first hand:{comp[0]}")
                if sum(user) > 21:
                    print(
                        f"Your Final Hand:{user}, Final Score:{sum(user)}\nComputer's Final Hand:{comp}, Final Score{sum(comp)} \nYOU WENT OVER 21. YOU LOST !!!"
                    )
                    end_of_game2=True
                elif sum(comp) > 21:
                    print(
                            f"Your Final Hand:{user}, Final Score:{sum(user)}\nComputer's Final Hand:{comp}, Final Score{sum(comp)} \nCOMPUTER WENT OVER 21. YOU WON !!!"
                        )
                    end_of_game2=True
            else:
                if sum(user) <= 21:
                    if sum(user) > sum(comp):
                        print(
                            f"Your Score:{sum(user)}, Computer's Score:{sum(comp)}\nYOU WON !!!"
                        )
                        end_of_game2=True
                    else:
                        print(
                            f"Your Score:{sum(user)}, Computer's Score:{sum(comp)}\nYOU LOST !!!"
                        )
                        end_of_game2=True

    elif start == "n":
        end_of_game = True
    else:
        print("Choose a valid command.")
