"""
Goal: Print a 10x10 multiplication table (1..10)
"""
for num in range(1, 11):
    for mult in range(1, 11):
        print(f'{num} x {mult} = {num * mult:2}', end='   ')
    print("")
