import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee  = Drink("Black coffee", 3.95)
        self.tea = Drink("Earl Grey", 2.00)
        self.customer = Customer("Tammy", 50)
    

        self.drinks = [self.coffee, self.tea]
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100, [self.coffee, self.tea])

    def test_coffee_shop_has_name(self):
        expected = "The Prancing Pony"
        actual = self.coffee_shop.name
        self.assertEqual(expected, actual)
        # also could be wrote ---- self.assertEqual("The Prancing Pony", self.coffee_shop.name)---its shorthand
        

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_coffee_shop_has_drink(self):
        self.assertEqual ([self.coffee, self.tea], self.coffee_shop.drinks)
        self.assertEqual(2, len(self.coffee_shop.drinks))
# alternative way to check a list
    def test_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)

    def test_decrease_till (self,):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)


