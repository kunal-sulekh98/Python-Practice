# report.py
#
# Exercise 2.4

import csv
import sys

if len(sys.argv) == 2:
    fn = sys.argv[1]
else:
    fn = "./Work/Data/portfolio.csv"

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio

print(portfolio_cost(fn))