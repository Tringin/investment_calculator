import matplotlib.pyplot as plt
from .simulation import get_monthly_progress


def create_investment_chart(monthly_progress_data, timeframe_data):
    monthly_progress_data = monthly_progress_data
    timeframe_data = timeframe_data
    plt.plot(len(monthly_progress_data), len(timeframe_data))
    plt.show()