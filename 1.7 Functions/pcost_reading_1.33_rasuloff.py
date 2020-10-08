# pcost.py
#
# Exercise 1.33: Reading from the command line

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                number_shares = int(row[1])
                price = float(row[2])
                total_cost += number_shares * price
            except ValueError:
                print('Warning - Error in row:', row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.srgv[1]
else:
    # or 'Data/portfolio.csv' if you run from terminal
    filename = 'C:/Users/Admin/Documents/Python/practical-python/Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost:', cost)
