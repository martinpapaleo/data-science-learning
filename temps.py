from datetime import date, timedelta
import random
from functools import reduce

# Generate 10 days of data: today, yesterday, ...
date_temp = []
n = 10
for i in range(10):
    day = date.today() - timedelta(days = i)
    date_temp.append(f"{day} -> {str(random.randint(15, 26))}°C.")

# Write to file as "YYYY-MM-DD -> temperature °C."
with open('temps.txt', 'w', encoding='utf-8') as file:
    for i in date_temp:
        file.write(i + '\n')

# Read back and compute stats
content = []
with open('temps.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        i = i.strip()
        if not i:
            continue

        # expect format "YYYY-MM-DD -> temperature °C."
        parts = i.split('->')
        if len(parts) != 2:
            continue
        try:
            temp_val = int(parts[1].strip()[:2])
        except ValueError:
            continue
        content.append(temp_val)

if content:
    average = round(sum(content) / len(content), 2)
    max_temp = max(content)
    print(f'Average temperature in the 10 days registered = {average}°C.\n'
          f'Max temperature in the 10 days registered = {max(content)}°C.')
else:
    print('No valid temperatures found.')
