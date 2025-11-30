'''
Goal: Start with 5 cities; append 2; remove 1; show first 3 via slicing.
'''
cities = ['Buenos Aires', 'Mar del Plata', 'Montevideo', 'CABA', 'Manhattan']
# Append exactly two
cities.append("Cancún")
cities.append("London")

# Remove one that exists
cities.remove("Buenos Aires")

# Keep a separate slice
first_three = cities[:3]

print("All cities:", cities)
print("First three:", first_three)