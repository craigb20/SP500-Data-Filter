class SP500Entry:
    def __init__(self, date, open_price, high_price, low_price, close_price):
        self.date = date
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.close_price = float(close_price)
