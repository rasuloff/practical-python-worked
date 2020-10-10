# report.py
#
# Exercise 2.6 Dictionaries as a container

'''
Write a function read_prices(filename) that reads a set of prices such as this into a dictionary
where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.

To do this, start with an empty dictionary and start inserting values into it just as you did above.
However, you are reading the values from a file now.

We’ll use this data structure to quickly lookup the price of a given stock name.
'''

import csv

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
prices = read_prices('Data/prices.csv')

from pprint import pprint
pprint(prices)

