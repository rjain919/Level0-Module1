"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import messagebox, simpledialog, Tk
import math
window = Tk()
window.withdraw()
N = simpledialog.askinteger('Hi', 'Name one number')
D = simpledialog.askinteger('Hi', 'Name a number')
messagebox.showinfo('Hi', 'Here is the sum of your numbers'+str(N+D))