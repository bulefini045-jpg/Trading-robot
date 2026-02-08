# Trading Configuration Settings

# Initial Capital
initial_capital = 10000  # Example: $10,000

# Risk Parameters
risk_per_trade = 0.01  # Risk 1% of total capital per trade
max_drawdown = 0.1  # Maximum drawdown allowed (10%)

# Position Sizing Rules
position_size = (initial_capital * risk_per_trade) // price_per_unit  # Calculate position size
