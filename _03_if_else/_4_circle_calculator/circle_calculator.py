# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

import turtle
from tkinter import messagebox, simpledialog, Tk
import math
window = Tk()
window.withdraw()
R = simpledialog.askinteger('Hi', 'What is the radius of a circle?')
C = simpledialog.askstring('Hi', 'Do you want to calculate the area or circumference of a circle?')
A = simpledialog.askstring('Hi', 'If you choose area, do you want the area of the circle displayed using the radius?')
CC = simpledialog.askstring('Hi', 'If you dont choose area, do you want the circumference displayed via the radius?')

