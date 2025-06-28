from modules.fees import get_transaction_fees

invested_capital = []

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    if initial_capital != 0:
        invested_capital = initial_capital
        invested_capital - get_transaction_fees(initial_capital)
        return invested_capital
    else:
        invested_capital = invested_capital + recurring_capital
        invested_capital - get_transaction_fees(invested_capital)
        return invested_capital