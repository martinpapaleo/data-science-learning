#1
all_v = [12, 0.2, "Hey", True, (1, 2, 3), {1, 2, 3}, {1: "A", 2: "B"}, [0, 1, "A", "B"]]
for i in all_v:
    print(f"The variable with value = {i} is type: {type(i)}")
#2
try:
    age = int(input("Insert age: "))
    if age < 0:
        print("Age cannot be negative.")
    elif age< 18:
            print("You are a minor.")
    else:
        print("Your are an adult.")
except ValueError:
    print("Age must be a valid number.")
#3
total_age = 0
for i in range(5):
    total_age += int(input("Insert age: "))
print(round(total_age / 5, 2))
#4
def calculate_statistics(lst):
    if len(lst) == 0:
        return 0, 0, 0
    else:
        from statistics import mean, median, mode
        try:
            return mean(lst), median(lst), mode(lst)
        except Exception as e:
            print(f"calculate_statistics received invalid list: {e}")

#5
def sum_(a,b):
    if not isinstance(a, int, float) or not isinstance(b, int, float):
        raise Exception("sum_ can only receive numbers as arguments")
    else:
        return a + b
def sub(a,b):
    if not isinstance(a, int, float) or not isinstance(b, int, float):
        raise Exception("sub can only receive numbers as arguments")
    else:
        return a - b
def mult(a, b):
    if not isinstance(a, int, float) or not isinstance(b, int, float):
        raise Exception("mult can only receive numbers as arguments")
    else:
        return a * b
def div(a, b):
    if not isinstance(a, int, float) or not isinstance(b, int, float):
        raise Exception("div can only receive numbers as arguments")
    else:
        return round(a / b, 2)
def valid_input(num):
    while True:
        try:
            return int(input(f"Type number {num}: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
try:
    num1 = valid_input("1")
    num2 = valid_input("2")
    action = valid_input("1 for addition, 2 for substraction, 3 for multiplication or 4 for division")
    if action == 1:
        print(f"{num1} + {num2} = {sum_(num1, num2)}")
    elif action == 2:
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif action == 3:
        print(f"{num1} * {num2} = {mult(num1, num2)}")
    elif action == 4:
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("None action taken.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

