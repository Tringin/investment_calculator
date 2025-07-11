import tkinter as tk

from .charts import create_investment_chart
from .config import DEFAULT_WINDOW_SIZE
from .simulation import *
from .charts import *

root = tk.Tk()
root.geometry(DEFAULT_WINDOW_SIZE)
root.title("Investment calculator")

# text for starting capital
tk.Label(root, text="Initial capital").grid(row=0, column=0)

# creating entry field and saving it in the variable. ofc also layout
entry_initial_capital = tk.Entry(root)
entry_initial_capital.grid(row=0, column=1)

# text for recurring capital
tk.Label(root, text="Recurring capital").grid(row=0, column=2)

# creating entry field and saving it in the variable. ofc also layout
entry_recurring_capital = tk.Entry(root)
entry_recurring_capital.grid(row=0, column=3)

# Rhythm + Dropdown-OptionMenu
tk.Label(root, text="Rhythm").grid(row=1, column=0)

rhythm_var = tk.StringVar()
rhythm_var.set("Monthly") # Default Value

options = ["Monthly", "Every 2 months", "Quarterly", "2x a year", "Yearly"]

dropdown = tk.OptionMenu(root, rhythm_var, *options)
dropdown.grid(row=1, column=1)

# Timeframe
tk.Label(root, text="Timeframe").grid(row=1, column=3)
entry_timeframe = tk.Entry(root)
entry_timeframe.grid(row=1, column=4)

# Return
tk.Label(root, text="Return (per month in %)").grid(row=2, column=3)
entry_return_value = tk.Entry(root)
entry_return_value.grid(row=2, column=4)

# PnL --> add here with config the pnl later
tk.Label(root, text="PnL").grid(row=6, column=0)
pnl_result = tk.Label(root, text="")
pnl_result.grid(row=6, column=1)

# Total fees --> add here with config the total fees later
tk.Label(root, text="Total Fees").grid(row=7, column=0)
total_fees = tk.Label(root, text="")
total_fees.grid(row=7, column=1)

def calculate_callback():
    initial = entry_initial_capital.get()
    recurring = entry_recurring_capital.get()
    rhythm = rhythm_var.get()
    timeframe = entry_timeframe.get()
    return_rate = entry_return_value.get()

    result = get_final_value(initial, recurring, rhythm, timeframe, return_rate)

    pnl_result.config(text=f"PnL: CHF {result}")

calculate_button = tk.Button(root, text="Calculate", command=calculate_callback)
calculate_button.grid(row=8, column=0)

def start_chart():
    initial = entry_initial_capital.get()
    recurring = entry_recurring_capital.get()
    rhythm = rhythm_var.get()
    timeframe = entry_timeframe.get()
    return_rate = entry_return_value.get()

    monthly_progress_data = get_monthly_progress(initial, recurring, rhythm, timeframe, return_rate)
    timeframe_data = entry_timeframe.get()
    create_investment_chart(monthly_progress_data, timeframe_data)

chart_button = tk.Button(root, text="Chart", command=start_chart)
chart_button.grid(row=8, column=1)