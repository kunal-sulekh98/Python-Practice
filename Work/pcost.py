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
        for row in rows:
            #li = line.split(',')
            try:
                share = int(row[1])
                price = float(row[2])
                result += share*price
            except ValueError:
                print("bakchodi chal rahi idhar!", line)

    return result

if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = "./Work/Data/portfolio.csv"

cost = portfolio_cost(fname)

print("Total cost: ",cost)
