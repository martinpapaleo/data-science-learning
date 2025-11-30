"""
Task: sets_1_unique.py
Goal: Show unique elements from a list using a set.
"""
x = [200, 1, 2, 2, 3, 4, 4, 5, 10]
w = set(x)

for i in sorted(w):
    print(i)
# Notes:
# - list: ordered, mutable sequence
# - tuple: ordered, immutable sequence
# - set: unordered, mutable collection of unique elements
