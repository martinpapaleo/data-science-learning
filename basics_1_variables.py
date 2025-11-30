#A
#1
v1 = 10
v2 = 12.2
v3 = "Phone"
v4 = True
v5 = [12, 'happy']
print(type(v1), type(v2), type(v3), type(v4), type(v5))
v1 = float(v1)
v3 = v3.upper()
#2
from datetime import date
def you_are_100(age, year):
    sol = year - int(age) + 100
    return sol
year = date.today().year
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hi {name}, you'll be 100 in the year {you_are_100(age,year)}.")
# Rubric
''' "5" + 2 fails because you can't sum two different type of objects, and "5" + "2" = "52" '''
