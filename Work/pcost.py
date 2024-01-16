# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import portfolio



def portfolio_cost(filename):

    
    cost = 0
    pfolio = portfolio(filename)
    #This above function makes a list of stock entries, each of which is a dictionary
    for stock in pfolio:
        cost += stock['shares']*stock['price']
    return cost
    
    """result = 0
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

    return result"""

def main(argv):
    fname = argv[1]
    cost = portfolio_cost(fname)
    print("Total cost: ",cost)
    

if __name__ == '__main__':
    import sys
    main(argv = sys.argv)
    

 


