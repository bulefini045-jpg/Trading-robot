import unittest

# Assuming MoneyManager and Portfolio are defined in trading_bot.py
from trading_bot import MoneyManager, Portfolio

class TestMoneyManager(unittest.TestCase):
    def setUp(self):
        self.manager = MoneyManager(initial_balance=1000)

    def test_initial_balance(self):
        self.assertEqual(self.manager.balance, 1000)

    def test_deposit(self):
        self.manager.deposit(500)
        self.assertEqual(self.manager.balance, 1500)

    def test_withdraw(self):
        self.manager.withdraw(300)
        self.assertEqual(self.manager.balance, 700)

    def test_overdraft(self):
        with self.assertRaises(ValueError):
            self.manager.withdraw(1200)


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio()

    def test_add_asset(self):
        self.portfolio.add_asset('AAPL', 10)
        self.assertIn('AAPL', self.portfolio.assets)
        self.assertEqual(self.portfolio.assets['AAPL'], 10)

    def test_remove_asset(self):
        self.portfolio.add_asset('AAPL', 10)
        self.portfolio.remove_asset('AAPL', 5)
        self.assertEqual(self.portfolio.assets['AAPL'], 5)

    def test_remove_nonexistent_asset(self):
        with self.assertRaises(ValueError):
            self.portfolio.remove_asset('GOOGL', 1)


if __name__ == '__main__':
    unittest.main()