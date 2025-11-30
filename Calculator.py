def ask_num():
    while True:
        num = input("Type in number: ")
        try:
            num = float(num)
            return num
        except ValueError:
            print("Error: Please type in any number without any letters or special characters: ")
def ask_op():
    while True:
        ops = ["sum", "sub", "mult", "div"]
        op = input("Type in operation (sum, sub, mult, div): ")
        if op in ops:
            return op
def calc(num_1, op, num_2):
    if op == "sum":
        return num_1 + num_2
    elif op == "sub":
        return num_1 - num_2
    elif op == "mult":
        return num_1 * num_2
    elif op == "div":
        if num_2 == 0:  # Handle division by zero
            return "Error: Division by zero is not allowed."
        else:
            return num_1 / num_2
    else:
        return "Error: Unsupported operation."

# Main
num1 = ask_num()
operation = ask_op()
num2 = ask_num()
result = calc(num1, operation, num2)
print(f"{num1} {operation} {num2} = {result}")
