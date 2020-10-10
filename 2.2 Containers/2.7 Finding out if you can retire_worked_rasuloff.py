# report.py
#
# Exercise 2.7 Finding out if you can retire

'''
Tie all of this work together by adding a few additional statements to your
report.py program that computes gain/loss. These statements should take the
list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6
and compute the current value of the portfolio along with the gain/loss.
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
            portfolio.append(stocks)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
            
        return prices  

# code below is to test and see if the above code works:

'''
Viewing large dictionaries and lists can be messy. To clean up the output for debugging,
consider using the pprint function.
'''
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

from pprint import pprint
pprint(portfolio)
pprint(prices)

# calculating the total cost

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print('Total cost of investment:', total_cost)

# calculating the current value

total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print('Current investment value:', total_value)

if total_value - total_cost > 0:
    print('Profit: ', total_value - total_cost)
elif total_value - total_cost < 0:
    print('Loss: ', total_value - total_cost)
else:
    print('No change in value', total_value - total_cost)
