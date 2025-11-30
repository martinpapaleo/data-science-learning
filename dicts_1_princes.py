'''
Goal: Maintain a dict of product prices; print keys and average price.
'''
def avg_price(prices: dict[str, float]) -> float:
    '''receives a dictonary with names and prices and returns the avg of those prices'''
    if not prices:
        raise ValueError('Cannot calculate average of empty dictionary.')
    return sum(prices.values()) / len(prices)
product_price = {'apple': 100, 'banana': 60}
product_price['orange'] = 80
keys_list = list(product_price.keys())
average = avg_price(product_price)

print(f"List of keys: {keys_list}. Average price = {average:.2f}.")