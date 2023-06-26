# Prime Number Checker
def check(number):
    for i in range(2, number):
        if number % i == 0:
            print(
                f"The number {number} is not a Prime Number, it is a Composite Number."
            )
        else:
            print(f"The number {number} is a Prime Number")
        break


num = int(input("Enter the Number you want to check whether is prime or not: "))
if num == 0:
    print("zero is neither defined as a Prime nor a Composite number")
if num == 2:
    print(f"The number {num} is a Prime Number")
else:
    check(num)