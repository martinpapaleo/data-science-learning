def ask_num():
    cond = False
    while not cond:
        cond = True
        num = input("Type a number: ")
        try:
            num = int(num)
            if num < 0:
                cond = False
            else:
                return num
        except ValueError:
            cond = False
def factorial(num):
    if not isinstance(num, int):
        raise Exception("factorial can only receive intigers")
    if num < 0:
        raise Exception("factorial can only receive positive numbers")
    if num == 0 or num == 1:
        return num
    else:
        sol = num
        sol *= factorial(num - 1)
    return sol
try:
    print(factorial(ask_num()))
except Exception as e:
    print(f"Error: {e}")

#Corrected version:

def ask_num():
    while True:
        num = input("Type a non-negative integer: ")
        try:
            num = int(num)
            if num < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

def factorial(num):
    if num == 0 or num == 1:  # Base case
        return 1
    else:
        return num * factorial(num - 1)  # Recursive case

# Main program flow
try:
    number = ask_num()  # Get user input
    print(f"The factorial of {number} is: {factorial(number)}")
except Exception as e:
    print(f"Error: {e}")