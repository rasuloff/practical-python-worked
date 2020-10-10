# report.py
#
# Exercise 2.10 Printing a formatted table

'''
Redo the for-loop in Exercise 2.9, but change the print statement to format the tuples.

>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
You can also expand the values and use f-strings. For example:

>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
Take the above statements and add them to your report.py program.
Have your program take the output of the make_report() function and print a nicely formatted table as shown.
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
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
            
        return prices

def make_report(portfolio, prices):
    rows = []
    for stocks in portfolio:
        current_price = prices[stocks['name']]
        change = current_price - stocks['price']
        total_summary = (stocks['name'], stocks['shares'], current_price, change)
        rows.append(total_summary)
    return rows

# code below is to test and see if the above code works:

'''
Viewing large dictionaries and lists can be messy. To clean up the output for debugging,
consider using the pprint function.
'''
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# report generation: it has to be put here after the portfolio and prices are generated with above codes

report = make_report(portfolio, prices)

# code to check if the above make_report and report codes work >>> MODIFIED per 2.10 exercise instructions <<<

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# normal print check for portfolio and prices

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
