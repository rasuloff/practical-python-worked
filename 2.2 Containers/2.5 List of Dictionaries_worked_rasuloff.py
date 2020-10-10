# report.py
#
# Exercise 2.5 A list of Dictionaries

'''
Take the function you wrote in Exercise 2.4 and modify to represent each stock in the portfolio with
a dictionary instead of a tuple. In this dictionary use the field names of “name”, “shares”, and “price”
to represent the different columns in the input file.
'''

import csv

def read_portfolio(filename):
    # opens a given portfolio file and reads it into a list of tuples
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stocks = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            # above stocks dictionary replaces this code: holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(stocks)
    return portfolio


# code below is to test and see if the above code works:

'''
Viewing large dictionaries and lists can be messy. To clean up the output for debugging,
consider using the pprint function.
'''
portfolio = read_portfolio('Data/portfolio.csv')

from pprint import pprint
pprint(prices)

# portfolio total cost calculation:

total = 0.0
for s in portfolio:
    total += s['shares'] * s['price'] # computation format changed to dict

print(total)
