# Rock Paper Siccors
import random

rock = """  
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
sissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
RPS = [rock, paper, sissor]
computer = random.choice(RPS)
player = input("choose one of the following:\n1.Rock\n2.Paper\n3.Siccors\n")
if player == "Rock" and "rock":
    print("you chose\n", rock)
    print("Computer chose", computer)
    if computer == sissor:
        print("you won")
    elif computer == player:
        print("its a draw")
    else:
        print("you lost")
elif player == "paper" and "paper":
    print("you chose\n", paper)
    print("Computer chose", computer)
    if computer == rock:
        print("you win")
    elif computer == player:
        print("its a draw")
    else:
        print("you lost")
elif player == "Siccor" and "sissor":
    print("you chose", sissor)
    print("Computer chose", computer)
    if computer == paper:
        print("you won")
    elif computer == player:
        print("its a draw")
    else:
        print("you lost")
else:
    print("Please enter a valid choice")