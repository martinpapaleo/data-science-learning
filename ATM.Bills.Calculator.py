'''
dic_ = {"Name": "Martin"}
print(dir(dic_))
dic_.update({"Country": "Argentina"})
print(dic_)'''
def calculate_bills_to_use(amount):
    bills = [500, 100, 50, 25, 10, 5, 1]
    sol = {}
    for bill in bills:
        key_, value_, quant = bill, 0, 0
        if bill <= amount:
            value_ = amount // key_
            amount -= (amount // key_) * bill
        sol.update({key_ : value_})
    return sol
def calculate_bills_to_use_advanced(amount, bills):
    sol = {}
    for bill in bills:
        if bill <= amount and bills[bill] != 0:
            if amount // bill <= bills[bill]:
                quant = amount // bill
            else:
                quant = bills[bill]
            sol[bill] = quant
            amount -= quant * bill
    return sol

print(calculate_bills_to_use(1376))
print(calculate_bills_to_use_advanced(163, {
        500: 1,
        100: 0,
        50: 10,
        25: 10,
        10: 0,
        5: 10,
        1: 10
    }))