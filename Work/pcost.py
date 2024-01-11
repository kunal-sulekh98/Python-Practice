# pcost.py
#
# Exercise 1.27

result = 0

with open('./Work/Data/portfolio.csv', 'rt') as f:
    h = next(f)
    for line in f:
        li = line.split(',')
        share = int(li[1])
        price = float(li[2][:-1])
        result += share*price

print(result)
