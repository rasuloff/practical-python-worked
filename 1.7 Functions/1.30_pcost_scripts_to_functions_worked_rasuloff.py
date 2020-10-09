# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            number_shares = int(row[1])
            price = float(row[2])
            total_cost += number_shares * price
    return total_cost

cost = portfolio_cost('Data/portfolio.csv') # this works if you run it in CMD or Terminal within the Work folder from course
print('Total Cost:', cost)

