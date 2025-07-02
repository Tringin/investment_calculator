import tkinter as tk
from decimal import Decimal
import matplotlib.pyplot as plt

from modules.gui import *
from modules.fees import get_transaction_fees

def get_fees_total():
    amount = initial_capital.get()
    amount = Decimal(amount)
    value = get_transaction_fees(amount)
    return value

# runs the main window loop
root.mainloop()