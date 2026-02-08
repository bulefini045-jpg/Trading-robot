# Risk Management and Position Sizing

class MoneyManager:
    def __init__(self, initial_balance, risk_per_trade=0.02):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.risk_per_trade = risk_per_trade  # 2% risk per trade
        self.trades = []
        self.max_position_size = 0.1  # Max 10% per position

    def calculate_position_size(self, entry_price, stop_loss_price):
        """Calculate position size based on risk"""
        risk_amount = self.current_balance * self.risk_per_trade
        price_difference = abs(entry_price - stop_loss_price)
        
        if price_difference == 0:
            return 0
        
        position_size = risk_amount / price_difference
        max_allowed = self.current_balance * self.max_position_size / entry_price
        
        return min(position_size, max_allowed)

    def execute_trade(self, asset, quantity, entry_price, stop_loss, take_profit):
        """Execute a trade and track it"""
        cost = quantity * entry_price
        
        if cost > self.current_balance:
            print("Insufficient balance for this trade")
            return False
        
        self.current_balance -= cost
        trade = {
            'asset': asset,
            'quantity': quantity,
            'entry_price': entry_price,
            'stop_loss': stop_loss,
            'take_profit': take_profit,
            'cost': cost,
            'status': 'open'
        }
        self.trades.append(trade)
        print(f"Trade executed: {quantity} of {asset} at ${entry_price}")
        return True

    def close_trade(self, trade_index, exit_price):
        """Close a trade and calculate profit/loss"""
        if trade_index >= len(self.trades):
            return False
        
        trade = self.trades[trade_index]
        profit_loss = (exit_price - trade['entry_price']) * trade['quantity']
        self.current_balance += trade['cost'] + profit_loss
        trade['status'] = 'closed'
        trade['exit_price'] = exit_price
        trade['profit_loss'] = profit_loss
        
        print(f"Trade closed: {trade['asset']} - Profit/Loss: ${profit_loss:.2f}")
        return True

    def get_account_stats(self):
        """Get overall account statistics"""
        total_profit_loss = sum(t.get('profit_loss', 0) for t in self.trades)
        win_rate = len([t for t in self.trades if t.get('profit_loss', 0) > 0]) / max(len(self.trades), 1)
        
        return {
            'current_balance': self.current_balance,
            'initial_balance': self.initial_balance,
            'total_profit_loss': total_profit_loss,
            'win_rate': win_rate,
            'total_trades': len(self.trades)
        }

if __name__ == '__main__':
    manager = MoneyManager(initial_balance=10000)
    
    # Example trade
    position_size = manager.calculate_position_size(entry_price=100, stop_loss_price=95)
    manager.execute_trade('BTC', position_size, 100, 95, 110)
    
    # Close trade
    manager.close_trade(0, 105)
    
    # Display stats
    stats = manager.get_account_stats()
    print("\nAccount Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")