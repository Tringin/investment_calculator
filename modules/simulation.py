from decimal import Decimal

portfolio_values = 0

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    return_rate = Decimal(str(return_rate))

    if initial_capital > 0:
        for months in range(1, timeframe, +1):
            if months % 1:
                portfolio_values = portfolio_values + recurring_capital