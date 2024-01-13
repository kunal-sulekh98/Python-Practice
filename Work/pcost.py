# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    result = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for no, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                result += nshares*price
            except ValueError:
                print("Row ",no,": Couldn't convert: ", row)

    return result

if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = "./Work/Data/portfolio.csv"

cost = portfolio_cost(fname)

print("Total cost: ",cost)
