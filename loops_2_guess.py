"""
Goal: User has 3 attempts to guess a random number 0..10.
"""
import random
number = random.randint(0, 10)
cond = False
count = 3
while not cond:
    try:
        num = int(input(f'Gess a number from 0-10: '))
    except ValueError:
        print('Please enter a valid intiger.')
        continue
    if not 0 <= num <= 10:
        print('Number must be between 0 and 10.')
        continue
    if num == number:
        cond = True
        print('Correct! You guessed it!')
    else:
        count -= 1
        print(f'Attempts left: {count}')
        if count == 0:
            cond = True
            print(f'Out of attempts! You lost!\n'
                  f'The number was {number}.')
