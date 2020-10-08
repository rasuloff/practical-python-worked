# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open('C:/Users/Admin/Documents/Python/practical-python/Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        number_shares = int(row[1])
        price = float(row[2])
        total_cost += number_shares * price

print("Total Cost", total_cost)

    
