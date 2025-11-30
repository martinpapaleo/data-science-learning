"""
Goal: Given a sentence, count words, vowels, and consonants.
"""

import string

VOWELS = set("aeiou")

def count_words(text: str) -> int:
    '''Counts words by splitting on whitespace.'''
    return len([w for w in text.split() if w])

def count_vowels(text: str) -> int:
    '''Counts vowel letters in the text (case-insensitive).'''
    count = 0
    for ch in text.lower():
        if ch in VOWELS:
            count += 1
    return count

def count_consonants(text: str) -> int:
    count = 0
    for ch in text.lower():
        if ch in string.ascii_lowercase and ch not in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    sentence = input('Type a sentence: ')

    words_am = count_words(sentence)
    vowels_am = count_vowels(sentence)
    consonats_am = count_consonants(sentence)

    print(
        f'The number of words in "{sentence}" is {words_am}.\n'
        f'The number of vowels is {vowels_am}.\n'
        f'The number of consonants is {consonats_am}'
    )
