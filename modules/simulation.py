from modules.fees import get_transaction_fees

portfolio_values = [0]

def calculate_investments(initial_capital, recurring_capital, rhythm, timeframe, return_rate):
    if rhythm == "Monthly":
        investments_per_year = 12
    elif rhythm == "Every 2 months":
        investments_per_year = 6
    elif rhythm == "Quarterly":
        investments_per_year = 4
    elif rhythm == "2x a year":
        investments_per_year = 2
    elif rhythm == "Yearly":
        investments_per_year = 1

    total_months = timeframe * 12
    investment_frequency = 12 // investments_per_year

    if initial_capital != 0:
        portfolio_values = portfolio_values + initial_capital
        portfolio_values = portfolio_values - get_transaction_fees(initial_capital)
        return portfolio_values
    else:
        portfolio_values = portfolio_values + recurring_capital
        portfolio_values = portfolio_values - get_transaction_fees(portfolio_values)
        return portfolio_values