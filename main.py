# Main Application - Run this to test your trading bot

from money_manager import MoneyManager
from portfolio import Portfolio

def main():
    print("=" * 60)
    print("🤖 TRADING BOT - MONEY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Initialize with $10,000
    manager = MoneyManager(initial_balance=10000, risk_per_trade=0.02)
    portfolio = Portfolio()
    
    print(f"\n💰 Starting Balance: ${manager.initial_balance:,.2f}")
    print(f"📊 Risk Per Trade: {manager.risk_per_trade * 100}%")
    print(f"📈 Max Position Size: {manager.max_position_size * 100}%")
    
    # ===== TRADE 1 =====
    print("\n" + "=" * 60)
    print("TRADE #1: BTC Purchase")
    print("=" * 60)
    
    entry_price_1 = 45000
    stop_loss_1 = 43000
    take_profit_1 = 47000
    
    # Calculate position size
    position_size_1 = manager.calculate_position_size(entry_price_1, stop_loss_1)
    print(f"\nEntry Price: ${entry_price_1:,.2f}")
    print(f"Stop Loss: ${stop_loss_1:,.2f}")
    print(f"Take Profit: ${take_profit_1:,.2f}")
    print(f"Position Size: {position_size_1:.4f} BTC")
    print(f"Investment: ${position_size_1 * entry_price_1:,.2f}")
    
    # Execute trade
    manager.execute_trade('BTC', position_size_1, entry_price_1, stop_loss_1, take_profit_1)
    portfolio.add_asset('BTC', position_size_1, entry_price_1)
    
    print(f"Current Balance: ${manager.current_balance:,.2f}")
    print(f"Portfolio Value: ${portfolio.total_value():,.2f}")
    
    # ===== TRADE 2 =====
    print("\n" + "=" * 60)
    print("TRADE #2: ETH Purchase")
    print("=" * 60)
    
    entry_price_2 = 2500
    stop_loss_2 = 2400
    take_profit_2 = 2600
    
    position_size_2 = manager.calculate_position_size(entry_price_2, stop_loss_2)
    print(f"\nEntry Price: ${entry_price_2:,.2f}")
    print(f"Stop Loss: ${stop_loss_2:,.2f}")
    print(f"Take Profit: ${take_profit_2:,.2f}")
    print(f"Position Size: {position_size_2:.4f} ETH")
    print(f"Investment: ${position_size_2 * entry_price_2:,.2f}")
    
    # Execute trade
    manager.execute_trade('ETH', position_size_2, entry_price_2, stop_loss_2, take_profit_2)
    portfolio.add_asset('ETH', position_size_2, entry_price_2)
    
    print(f"Current Balance: ${manager.current_balance:,.2f}")
    print(f"Portfolio Value: ${portfolio.total_value():,.2f}")
    
    # ===== CLOSE TRADE 1 (PROFIT) =====
    print("\n" + "=" * 60)
    print("CLOSING TRADE #1: BTC at PROFIT")
    print("=" * 60)
    
    exit_price_1 = 46500
    print(f"\nExit Price: ${exit_price_1:,.2f}")
    manager.close_trade(0, exit_price_1)
    
    print(f"Current Balance: ${manager.current_balance:,.2f}")
    
    # ===== CLOSE TRADE 2 (LOSS) =====
    print("\n" + "=" * 60)
    print("CLOSING TRADE #2: ETH at LOSS")
    print("=" * 60)
    
    exit_price_2 = 2450
    print(f"\nExit Price: ${exit_price_2:,.2f}")
    manager.close_trade(1, exit_price_2)
    
    print(f"Current Balance: ${manager.current_balance:,.2f}")
    
    # ===== FINAL ACCOUNT STATISTICS =====
    print("\n" + "=" * 60)
    print("📊 FINAL ACCOUNT STATISTICS")
    print("=" * 60)
    
    stats = manager.get_account_stats()
    
    print(f"\nStarting Balance:    ${stats['initial_balance']:,.2f}")
    print(f"Current Balance:     ${stats['current_balance']:,.2f}")
    print(f"Total Profit/Loss:   ${stats['total_profit_loss']:,.2f}")
    
    roi = ((stats['current_balance'] - stats['initial_balance']) / stats['initial_balance']) * 100
    print(f"ROI (Return):        {roi:.2f}%")
    
    print(f"\nTotal Trades:        {stats['total_trades']}")
    print(f"Win Rate:            {stats['win_rate'] * 100:.1f}%")
    
    # Color coding
    if stats['total_profit_loss'] > 0:
        status = "✅ PROFITABLE"
    else:
        status = "❌ LOSS"
    
    print(f"\nStatus: {status}")
    print("=" * 60)

if __name__ == "__main__":
    main()