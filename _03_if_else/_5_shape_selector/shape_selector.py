import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Teal=turtle.Turtle()
    S = simpledialog.askstring('Hi', 'What shape do you want to draw?')
    if S == "square":
        for i in range(4):
            Teal.forward(100)
            Teal.right(90)
    elif S == "rectangle":
        for i in range(4):
            Teal.forward(150)
            Teal.right (90)
    elif S == "triangle":
        for i in range(3):
            Teal.forward(100)
            Teal.left(120)
    turtle.done()
    
    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
