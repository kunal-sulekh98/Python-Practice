# report.py
#
# Exercise 2.4

import csv

from fileparse import parse_csv

def portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #print(row)
            row[1] = int(row[1])
            row[2] = float(row[2])
            stock = dict(zip(headers,row))
            #print(stock)
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
        change = price - float(stock['price'])
        report.append((name, shares, price, round(change,2)))

    return report

from pprint import pprint


#pfolio = portfolio("./Work/Data/portfolio.csv")
#prices = read_prices("./Work/Data/prices.csv")
#report = make_report(pfolio, prices)

def portfolio_report(p_file, prices_file):
    pfolio = parse_csv(p_file)

    prices = read_prices(prices_file)
    rep = make_report(pfolio, prices)
    
    headers = "Names","Shares","Prices", "Changes"
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(headers[0], headers[1], headers[2], headers[3]))
    gap = "----------"
    print((gap+" ")*4)

    for row in rep:
        print('{:>10s} {:>10d} {:>10s} {:10.2f}'.format(row[0], row[1], '$'+str(round(row[2],2)), row[3]))




#portfolio_report('./Data/portfolio2.csv', './Data/prices.csv')



"""total_cost = 0.0
for stock in pfolio:
    total_cost += stock['shares'] * stock['price']

total_value = 0.0
for stock in pfolio:
    total_value += stock['shares'] * prices[stock['name']]"""



