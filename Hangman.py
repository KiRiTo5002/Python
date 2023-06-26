# Hangman game Fruit edition
import random


display = []
lives = 6

stages = [
    """
  +---+
  |   |
  O   |
 /|\  | 
 / |  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

logo = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ | / _` | '_ | / _` | '_ ` _ | / _` | '_ | 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_||__,_|_| |_||__, |_| |_| |_||__,_|_| |_|
                    __/ |                      
                   |___/    """

words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "pineapple",
    "mango",
    "kiwi",
    "pear",
    "strawberry",
    "watermelon",
    "blueberry",
    "cherry",
    "lemon",
    "peach",
    "plum",
    "raspberry",
    "apricot",
    "blackberry",
    "coconut",
    "fig",
    "guava",
    "lime",
    "pomegranate",
    "avocado",
    "melon",
    "papaya",
    "cantaloupe",
    "cranberry",
    "date",
    "elderberry",
    "gooseberry",
    "kiwifruit",
    "lychee",
    "nectarine",
    "passion fruit",
    "persimmon",
    "quince",
    "tangerine",
    "boysenberry",
    "durian",
    "grapefruit",
    "honeydew",
    "jackfruit",
    "kumquat",
    "mangosteen",
    "mulberry",
    "olive",
    "rhubarb",
    "star fruit",
    "tomato",
]


print(logo)
print("A random word has been chosen, Try your best to guess the word-->")
ch_word = random.choice(words)
length = len(ch_word)
end = False
for i in range(length):
    display += "_"
result = "".join(display)
while end == False:
    print("".join(display))
    guess = input("Guess A Letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter{guess}.")
    for i in range(length):
        if guess == ch_word[i]:
            display[i] = guess
            print("Correct Guess!!!\n----<><><>----")

    if guess not in ch_word:
        print(
            f"The letter '{guess}' was not in the word, You loose a life :( \n----<><><>----"
        )
        lives -= 1
        print(stages[6 - lives])
        print("lives remaining:", lives)
        if lives == 0:
            print("You Loose!\nThe word was", ch_word)
            end = True
    if "_" not in display:
        print("".join(display))
        print("yay! You Won\nThe word was", ch_word)
        end = True