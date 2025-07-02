from decimal import Decimal
from .fees import get_transaction_fees
from .config import RHYTHM_MAPPING
from .gui import *

portfolio_values = 0

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    return_rate = Decimal(str(return_rate))

    if initial_capital != 0:
        portfolio_values = initial_capital
        for months in range(1, timeframe + 1):
            if months % RHYTHM_MAPPING[rhythm] == 0:
                recurring_capital -= get_transaction_fees(recurring_capital)
                portfolio_values += recurring_capital
                if months != 1:
                    monthly_return = return_rate / timeframe
                    portfolio_values = portfolio_values * (1 + monthly_return)
        return portfolio_values

def calculate_callback():
    initial = entry_initial_capital.get()
    recurring = entry_recurring_capital.get()
    rhythm = rhythm_var.get()
    timeframe = entry_timeframe.get()
    return_rate = entry_return_value.get()

    result = calculate_investments(initial, recurring, rhythm, timeframe, return_rate)

    pnl_result.config(text=f"PnL: {result}")