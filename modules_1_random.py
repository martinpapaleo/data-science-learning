"""
Goal: Read movie names from a file and print one random movie.
"""
import random
lst = []
with open('5_movies.txt', 'r', encoding='utf-8') as file:
    for i in file:
        movie = i.strip()
        if movie:
            lst.append(movie)
if not lst:
    print('No movies found in the file.')
else:
    choice = random.choice(lst)
    print(f'One random movie from the file is: {choice}')

# File modes:
# 'r'  -> read
# 'w'  -> write (overwrites file)
# 'a'  -> append (adds to the end of file)
