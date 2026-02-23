'''
Clean:

- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
- Ensure numeric columns are numeric (no silent object leftovers)
'''

import os
import pandas as pd

print("cwd:", os.getcwd())
print("__file__:", __file__)