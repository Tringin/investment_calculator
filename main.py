import tkinter as tk
from decimal import Decimal

import matplotlib.pyplot as plt

from modules.fees import get_transaction_fees
#from modules.simulation import FUNKTIONEN

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

def get_capital():
    amount = initial_capital.get()
    amount = Decimal(amount)
    value = get_transaction_fees(amount)
    output_label.config(text=f"Gebühren: CHF {value}")


#runs the main window loop
root.mainloop()