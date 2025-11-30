import string


def shift_letters(letters, shift):
    return letters[shift:] + letters[:shift]
def encrypt_simple(letters, shift):
    original_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    shifted_lst = original_lst[s hift:] + original_lst[:shift]
    sol = ''
    for letter in letters:
        for element in range(len(original_lst)):
            if original_lst[element] == letter:
                sol += shifted_lst[element]
    return sol

#Global Code

letters_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
print(shift_letters(letters_lst, 6))
print(encrypt_simple('DATAWARS', -14))


print(string.ascii_uppercase)
print(string.ascii_lowercase)