# report.py
#
# Exercise 2.4 A list of tuples

import csv

def read_portfolio(filename):
    # opens a given portfolio file and reads it into a list of tuples
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
portfolio

total = 0.0
for name, shares, price in portfolio:
    total += shares * price

print(total)
