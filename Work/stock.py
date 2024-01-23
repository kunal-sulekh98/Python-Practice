
class Stock:

    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, sold):
        self.shares -= sold

    def __repr__(self):
        return f'Stock ( Name: {self.name} ; Shares: {self.shares} ; Price: {self.price} )'
    
    def __str__(self):
        return f'STOCK ( Name: {self.name} ; Shares: {self.shares} ; Price: {self.price} )'
        