import tkinter as tk
from decimal import Decimal
import matplotlib.pyplot as plt

from modules.gui import *
from modules.simulation import calculate_investments

calculate_investments(entry_initial_capital, entry_recurring_capital, rhythm_var, entry_timeframe, entry_return_value)



# runs the main window loop
root.mainloop()