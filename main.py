import tkinter as tk
from decimal import Decimal
import matplotlib.pyplot as plt

from modules.fees import get_transaction_fees
#from modules.simulation import FUNCTION

root = tk.Tk()
root.geometry("800x600")
root.title("Investment calculator")

#text for recurring capital
tk.Label(root, text="Recurring capital").grid(row=0, column=0)

#creating entry field and saving it in the variable. ofc also layout
recurring_capital = tk.Entry(root)
recurring_capital.grid(row=0, column=1)

#text for starting capital
tk.Label(root, text="Initial capital").grid(row=0, column=2)

#creating entry field and saving it in the variable. ofc also layout
initial_capital = tk.Entry(root)
initial_capital.grid(row=0, column=3)

#Rhythm + ticking boxes
tk.Label(root, text="Rhythm").grid(row=1, column=0)

rhythm_box1 = tk.Radiobutton(root)
rhythm_box1.grid(row=1, column=2)
tk.Label(root, text="Monthly").grid(row=1, column=1)

rhythm_box2 = tk.Radiobutton(root)
rhythm_box2.grid(row=2, column=2)
tk.Label(root, text="Every 2 months").grid(row=2, column=1)

rhythm_box3 = tk.Radiobutton(root)
rhythm_box3.grid(row=3, column=2)
tk.Label(root, text="Quarterly").grid(row=3, column=1)

rhythm_box4 = tk.Radiobutton(root)
rhythm_box4.grid(row=4, column=2)
tk.Label(root, text="2x a year").grid(row=4, column=1)

rhythm_box5 = tk.Radiobutton(root)
rhythm_box5.grid(row=5, column=2)
tk.Label(root, text="Yearly").grid(row=5, column=1)

#Timeframe
tk.Label(root, text="Timeframe").grid(row=1, column=3)
timeframe_value = tk.Entry(root)
timeframe_value.grid(row=1, column=4)

#Return
tk.Label(root, text="Return (p.a. in %)").grid(row=2, column=3)
return_value = tk.Entry(root)
return_value.grid(row=2, column=4)

#PnL --> add here with config the pnl later
tk.Label(root, text="PnL").grid(row=6, column=0)
pnl_result = tk.Label(root, text="")
pnl_result.grid(row=6, column=1)

#Total fees --> add here with config the total fees later
tk.Label(root, text="Total Fees").grid(row=7, column=0)
total_fees = tk.Label(root, text="")
total_fees.grid(row=7, column=1)


def get_fees_total():
    amount = initial_capital.get()
    amount = Decimal(amount)
    value = get_transaction_fees(amount)
    return value

#runs the main window loop
root.mainloop()