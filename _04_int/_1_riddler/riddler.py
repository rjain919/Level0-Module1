
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct

Riddle: The more you take, the more you leave behind. What am I?
Answer: Footsteps.

Riddle: What 8 letter word can have a letter taken away and it still makes a word. Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?
Answer: The word is starting! starting, staring, string, sting, sing, sin, in, I.  Cool,huh?

Riddle: Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
Answer: Yesterday, Today, and Tomorrow.

"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
S = 0
A = simpledialog.askstring('Hi', 'The more you take, the more you leave behind. What am I?')
R = simpledialog.askstring('Hi', 'What 8 letter word can have a letter taken away and it still makes a word. Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?')
Q = simpledialog.askstring('Hi', 'Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
if A == 'footsteps':
    S+=1
if R == 'starting':
    S+=1
if Q == 'Yesterday, today, tomorrow':
    S+=1
messagebox.showinfo('Hi', 'Here is your final score.'+S)
