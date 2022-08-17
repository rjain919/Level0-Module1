import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    RP = simpledialog.askinteger('Hi', 'What is the radius in pixels?')
    # Make a new turtle
    Teal=turtle.Turtle()
    Teal.circle(RP)
    Teal.penup()
    Teal.goto(64, 32)
    A = math.pi*RP*RP
    Teal.write(A)
    
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()

    # Call the turtle .penup() method

    # Move your turtle to a new x,y position using .goto()

    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
    Teal.write(arg="area = " + str(A), move=True, align='left', font=('Arial',8,'normal'))
    Teal.hideturtle()
    turtle.done()
    # Hide your turtle

    # Call turtle.done()
