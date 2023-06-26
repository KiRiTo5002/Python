# Encryption and Decryption Program
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
    " ",
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
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
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


def encrypt(text_a, shift_a):
    for letter in text_a:
        indent = letters.index(letter)
        letter = letters[indent + shift_a]
        print(letter, end="")


def decrypt(text_a, shift_a):
    for letter in text_a:
        indent = letters.index(letter)
        letter = letters[indent - shift_a]
        print(letter, end="")


end_of_program = False
while end_of_program == False:
    choice = input(
        "Do you want to encrypt or decrypt? Type 'enc' for encryption and 'dec' for decryption:\n-->"
    )
    if choice == "enc":
        text = input("Type your text:\n-->").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
        choice_2 = input(
            "\nDo you want to continue?\n Type 'yes' to continue and 'no' to abort\n-->"
        )
        if choice_2 == "yes":
            end_of_program = False
        else:
            end_of_program = True
            print("\nThank you for using.")
    elif choice == "dec":
        text = input("Type your text:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
        choice_2 = input(
            "\nDo you want to continue?\n Type 'yes' to continue and 'no' to abort\n-->"
        )
        if choice_2 == "yes":
            end_of_program = False
        else:
            end_of_program = True
            print("Thank you for using.")
    else:
        print("Please choose a valid command")