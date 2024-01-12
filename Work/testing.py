
"""with open('./Work/Data/portfolio.csv', 'rt') as f:
        data = f.read()"""

with open('./Work/Data/portfolio.csv', 'rt') as f:
        for line in f:
            fields = line.split(',')
            try:
                shares = int(fields[1])
            except ValueError:
                print("Couldn't parse", line)
            
