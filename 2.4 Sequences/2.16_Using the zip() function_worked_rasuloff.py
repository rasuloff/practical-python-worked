# pcost.py
#
# Exercise 2.16: Using the zip() function

'''
Recall that the file Data/missing.csv contains data for a stock portfolio,
but has some rows with missing data. Using enumerate(), modify your pcost.py
program so that it prints a line number with the warning message when it
encounters bad input.
'''

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            # row = line.split(',')
            try:
                number_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += number_shares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

if len(sys.argv) == 2:
    filename = sys.srgv[1]
else:
    filename = input('Data/portfoliodate.csv')

cost = portfolio_cost(filename)
print('Total Cost:', cost)
