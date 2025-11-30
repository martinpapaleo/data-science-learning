'''
Goal: create a dictionary of expense categories and totals
       until the user types 'quit', then save a summary to CSV.
'''

#validate price
def valid_price() -> float:
    """Ask the user for a price and return it as a positive float."""
    while True:
        price_str = input('Enter a valid price: ').strip()
        try:
            value = float(price_str)
        except ValueError:
            print('Valid price must be entered.')
            continue
        if value < 0:
            print('Price cannot be negative.')
            continue
        return value
# add key-value pairs to a dictionary:
def add_dict(expenses: dict, category: str, amount: float) -> dict:
    """Add amount to a category in the expenses dict."""
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    return expenses

# Receives empty dictionary and returns it based on user input
def valid_dictionary(expenses: dict) -> dict:
    """
    Ask the user for categories and prices until they type 'quit'.
    Returns the filled dictionary.
    """
    while True:
        category = input('Enter a key: ').strip()
        if not category:
            print('Valid category must be entered.')
            continue
        if category.lower() == 'quit':
            return expenses
        price = valid_price()
        expenses = add_dict(expenses, category.title(), price)

# main
if __name__ == '__main__':
    expenses = valid_dictionary({})
    if expenses:
        with open('budget_tracker.csv', 'w', encoding='utf-8') as file:
            file.write(f'Total expenses = {sum(expenses.values())}\n')
            for keys in expenses:
                file.write(f'{keys}: {expenses[keys]}\n')
        print('Budget saved to budget_tracker.csv')
    else:
        print('No expenses entered. No CSV file needed.')
