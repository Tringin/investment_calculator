from decimal import Decimal
from .fees import get_transaction_fees
from .config import RHYTHM_MAPPING

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    recurring_capital -= get_transaction_fees(recurring_capital)
    return_rate = int(str(return_rate))
    timeframe = int(timeframe)
    monthly_return = (1 + return_rate / 100) ** (1/12) - 1

    if initial_capital != 0:
        portfolio_values = initial_capital
        portfolio_values -= get_transaction_fees(portfolio_values)
        for months in range(1, timeframe + 1):
            portfolio_values = portfolio_values + monthly_return
            print(portfolio_values)
            if months % RHYTHM_MAPPING[rhythm] == 0:
                portfolio_values += recurring_capital
    return portfolio_values