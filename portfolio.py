# Portfolio Management and Money Tracking

class Portfolio:
    def __init__(self):
        self.assets = {}

    def add_asset(self, asset_name, quantity, price_per_unit):
        self.assets[asset_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}
        print(f'Added {quantity} of {asset_name} at ${price_per_unit} per unit.')

    def remove_asset(self, asset_name):
        if asset_name in self.assets:
            del self.assets[asset_name]
            print(f'Removed {asset_name} from portfolio.')
        else:
            print(f'{asset_name} not found in portfolio.')

    def total_value(self):
        total = 0
        for asset, info in self.assets.items():
            total += info['quantity'] * info['price_per_unit']
        return total

    def display_portfolio(self):
        for asset, info in self.assets.items():
            print(f'{asset}: {info['quantity']} units at ${info['price_per_unit']} each')

if __name__ == '__main__':
    portfolio = Portfolio()
    portfolio.add_asset('AAPL', 10, 150.00)
    portfolio.add_asset('GOOGL', 5, 2800.00)
    portfolio.display_portfolio()
    print(f'Total Portfolio Value: ${portfolio.total_value()}')