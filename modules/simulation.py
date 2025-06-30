from decimal import Decimal
from fees import get_transaction_fees

portfolio_values = 0

rhythm_in_months = {
    "Monthly": 1,
    "Every 2 months": 2,
    "Quarterly": 3,
    "2x a year": 6,
    "Yearly": 12
}

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    initial_capital = Decimal(str(initial_capital))
    recurring_capital = Decimal(str(recurring_capital))
    return_rate = Decimal(str(return_rate))

    if initial_capital != 0:
        portfolio_value = initial_capital
        for months in range(1, timeframe + 1):
            if months % rhythm_in_months[rhythm] == 0:
                recurring_capital -= get_transaction_fees(recurring_capital)
                portfolio_values += recurring_capital
                if months != 1:
                    monthly_return = return_rate / timeframe
                    portfolio_values = portfolio_values * (1 + monthly_return)