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

def make_report(prtfolio, prices):
    report = []
    for stock in prtfolio:
        name = stock['name']
        shares = stock['shares']
        price = prices[stock['name']]
        change = price - stock['price']
        report.append((name, shares, price, round(change,2)))

    return report

from pprint import pprint


pfolio = portfolio("./Work/Data/portfolio.csv")
prices = read_prices("./Work/Data/prices.csv")
report = make_report(pfolio, prices)

total_cost = 0.0
for stock in pfolio:
    total_cost += stock['shares'] * stock['price']

total_value = 0.0
for stock in pfolio:
    total_value += stock['shares'] * prices[stock['name']]


headers = "Names","Shares","Prices", "Changes"
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(headers[0], headers[1], headers[2], headers[3]))
gap = "----------"
print((gap+" ")*4)


for row in report:
    print('{:>10s} {:10d} {:>10s} {:10.2f}'.format(row[0], row[1], '$'+str(round(row[2],2)), row[3]))

#print('Current value', total_value)
#print('Gain', f"{ total_value - total_cost :.2f}")

#pprint(prices)
