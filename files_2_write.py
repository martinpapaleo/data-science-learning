"""
Goal: Ask the user for 5 movie names and write them to a file, one per line.
"""
movies = []
for i in range(5):
    movies.append(input('Enter a movie name: '))
with open('5_movies.txt', 'w', encoding='utf-8') as file:
    for i in movies:
        file.write(i + '\n')