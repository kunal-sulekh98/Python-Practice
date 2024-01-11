
"""with open('./Work/Data/portfolio.csv', 'rt') as f:
        data = f.read()"""

with open('./Work/Data/portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')
