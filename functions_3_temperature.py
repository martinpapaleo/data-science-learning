def c_to_f(c: float) -> float:
    '''Converts Celcius to Farenheit.'''
    return c * (9/5) + 32
while __name__ == '__main__':
        try:
            c_str = input('Enter Celcius degrees: ')
            c_val = float(c_str)
        except ValueError:
            print('Please enter a valid number.')
            continue
        else:
            f = c_to_f(c_val)
            print(f"{c_val:.1f} Celsius equals {f:.1f} Fahrenheit.")
            break