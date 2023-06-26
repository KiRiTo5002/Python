# A better calculator
ui = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""


def add(n1, n2):
    """Takes in arguements and gives the sum."""
    return n1 + n2


def subtract(n1, n2):
    """Takes in arguements and gives the difference."""
    return n1 - n2


def multiply(n1, n2):
    """Takes in arguements and gives out the product."""
    return n1 * n2


def divide(n1, n2):
    """Takes in arguement and gives out the quotient"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
end_of_program = False
num1 = int(input("Enter the first number\n---->"))
while end_of_program == False:
    for operators in operations:
        print(operators)
    operator = input("Choose an operator from above list:\n---->")
    num2 = int(input("Enter the second number:\n---->"))
    calculation_op = operations[operator]
    answer1 = calculation_op(num1, num2)
    print(f"{num1}{operator}{num2}={answer1}")
    num1 = answer1
    choice = input(
        f"Do you want to continue calculating with{answer1}?.Type 'y' for yes and 'n' for no.\n---->"
    )
    if choice == "y":
        continue
    else:
        break