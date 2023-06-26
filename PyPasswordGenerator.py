# py-password generator
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
password = []
lengthL = int(input("Enter the desired number of letters:\n"))
for i in range(lengthL + 1):
    lett = random.choice(letters)
    password.append(lett)
sym = int(input("Enter the number of symbols you would like in your password.\n"))
for i in range(sym + 1):
    symb = random.choice(symbols)
    password.append(symb)
num = int(input("Enter the number of numbers you would like in your password.\n"))
for i in range(num):
    numb = random.choice(numbers)
    password.append(numb)
random.shuffle(password)
for i in password:
    print("your password would be: ", i, end="")