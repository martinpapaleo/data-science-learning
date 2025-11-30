"""
Goal: Write a list of ITBA careers to a file and print each line in uppercase.
"""

itba_careers = [
    "Lic Data Science",
    "Lic Business & Management",
    "Mechanical Engineering",
    "Industrial Engineering",
    "Biomedical Engineering",
]
# Write file
with open('ITBA_Careers.txt', 'w', encoding='utf-8') as file:
    for i in itba_careers:
        file.write(i + '\n')

# Read and print uppercased
with open('ITBA_Careers.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i.rstrip().upper())
