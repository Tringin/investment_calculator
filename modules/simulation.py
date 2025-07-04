from decimal import Decimal
from .fees import get_transaction_fees
from .config import RHYTHM_MAPPING

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    recurring_capital -= get_transaction_fees(recurring_capital)
    return_rate = int(return_rate)
    timeframe = int(timeframe)

    monthly_values = []

    if initial_capital != 0:
        portfolio_values = initial_capital - get_transaction_fees(initial_capital)
    else:
        portfolio_values = recurring_capital - get_transaction_fees(recurring_capital)

    for months in range(1, timeframe + 1):
        portfolio_values = portfolio_values + (portfolio_values / 100 * return_rate)

        if months % RHYTHM_MAPPING[rhythm] == 0:
            portfolio_values += recurring_capital

        monthly_values.append(round(portfolio_values, 2))

    return monthly_values

def get_final_value(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    values = calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate)
    return values[-1] if values else Decimal('0')

def get_monthly_progress(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    return calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate)