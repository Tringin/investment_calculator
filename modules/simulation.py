from decimal import Decimal
from .fees import get_transaction_fees
from .config import RHYTHM_MAPPING

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    recurring_capital -= get_transaction_fees(recurring_capital)
    return_rate = int(return_rate)
    timeframe = int(timeframe)

    if initial_capital != 0:
        portfolio_values = initial_capital
        portfolio_values -= get_transaction_fees(portfolio_values)
    else:
        portfolio_values = recurring_capital
        portfolio_values -= get_transaction_fees(portfolio_values)
    for months in range(1, timeframe + 1):
        portfolio_values = portfolio_values + (portfolio_values / 100 * return_rate)
        if months % RHYTHM_MAPPING[rhythm] == 0:
            portfolio_values += recurring_capital
    return round(portfolio_values, 2)

def calculate_monthly_progress(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    recurring_capital -= get_transaction_fees(recurring_capital)
    return_rate = int(return_rate)
    timeframe = int(timeframe)

    all_returns = []

    if initial_capital != 0:
        portfolio_values = initial_capital
        portfolio_values -= get_transaction_fees(portfolio_values)
    else:
        portfolio_values = recurring_capital
        portfolio_values -= get_transaction_fees(portfolio_values)
    for months in range(1, timeframe + 1):
        portfolio_values = portfolio_values + (portfolio_values / 100 * return_rate)
        if months % RHYTHM_MAPPING[rhythm] == 0:
            portfolio_values += recurring_capital
        all_returns.append(round(portfolio_values, 2))
    return all_returns