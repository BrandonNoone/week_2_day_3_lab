class CoffeeShop:
	
	def __init__(self, name, till, drinks):
		self.name = name
		self.till = till
		self.drinks = drinks

	def change_till_by_amount(self, amount):
		self.till += amount

	def sell_drink(self, drink_to_sell):
		self.till += drink_to_sell.price