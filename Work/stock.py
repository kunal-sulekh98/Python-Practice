
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

    def __repr__(self):
        return f'Stock ( Name: {self.name} ; Shares: {self.shares} ; Price: {self.price} )'
    
    def __str__(self):
        return f'STOCK ( Name: {self.name} ; Shares: {self.shares} ; Price: {self.price} )'
        