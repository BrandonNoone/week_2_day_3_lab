import unittest
from src.customer import Customer
from src.drink import Drink

class Testcustomer(unittest.TestCase):
    def setUp(self):
        self.tammy = Customer("Tammy", 50)
        self.water = Drink("Spring Water", 10)

    def test_customer_has_name(self):
        self.assertEqual("Tammy", self.tammy.name)
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.tammy.wallet)


    def test_customer_can_buy_drink(self):
        self.tammy.buy_drink(self.water)
        self.assertEqual(40, self.tammy.wallet)


