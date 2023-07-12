class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price 