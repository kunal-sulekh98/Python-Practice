
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        self.cost = self.shares * self.price
        return self.cost
    
    def sell(self, sold):
        self.shares -= sold