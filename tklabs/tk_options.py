"""
This demo adapted from a tutorial at:

https://www.pythontutorial.net/tkinter/tkinter-options/
"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Using keyword arguments when creating the widget
ttk.Label(root, text='Hi, there; I was made using keyword arguments').pack()

# Using a dictionary index after widget creation
label = ttk.Label(root)
label['text'] = 'Hi, there; I was made using a dictionary index after widget creation'
label.pack()

# Using the config() method with keyword attributes
label2 = ttk.Label(root)
label2.config(text='Hi, there; I was made using the config() method')
label2.pack()


root.mainloop()

"""
In conclusion.  Ttk widgets provide you with three ways to set options:

-Use keyword arguments at widget creation
-Use a dictionary index after widget creation
-Use the config() method with keyword attributes
"""
