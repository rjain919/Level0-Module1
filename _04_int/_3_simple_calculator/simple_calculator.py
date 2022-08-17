"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
import math
window = Tk()
window.withdraw()
D = simpledialog.askinteger('Hi', 'Can I have one number')
N = simpledialog.askinteger('Hi', 'Can you name one number')
ASMD = simpledialog.askstring('Hi', 'Do you want to add, subtract, multiply, or divide?')
if ASMD == 'add':
    sum = D + N
elif ASMD == 'subtract':
    sum = D - N
elif ASMD == 'multiply':
    sum = D * N
elif ASMD == 'Divide':
    sum = D/N
messagebox.showinfo('Hi', 'Here are your results'+str(sum))