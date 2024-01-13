# report.py
#
# Exercise 2.4

import csv

def portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {}
            stock['name'] = row[0]
            stock['shares'] = int(row[1])
            stock['price'] = float(row[2])
            portfolio.append(stock)
    return portfolio


def read_prices(filename):
    with open(filename, 'rt') as fn:
        rows = csv.reader(fn)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
        return prices

        

from pprint import pprint


pfolio = portfolio("./Work/Data/portfolio.csv")
prices = read_prices("./Work/Data/prices.csv")

total_cost = 0.0
for stock in pfolio:
    total_cost += stock['shares'] * stock['price']

total_value = 0.0
for stock in pfolio:
    total_value += stock['shares'] * prices[stock['name']]


print('Current value', total_value)
print('Gain', f"{ total_value - total_cost :.2f}")

#pprint(prices)
