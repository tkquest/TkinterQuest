"""
This file based on tutorial at:

https://www.pythontutorial.net/tkinter/tkinter-window/
"""

"""
BLUF -- a quick summary:
Use the title() method to change the title of the window.
Use the geometry() method to change the size and location of the window.
Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
Use the window.attributes('-alpha',0.5) to set the transparency for the window.
Use the window.attributes('-topmost', 1) to make the window always on top.
Use lift() and lower() methods to move the window up and down of the window stacking order.
Use the iconbitmap() method to change the default icon of the window.
"""


import tkinter as tk

root = tk.Tk()

# --- CHANGING THE WINDOW TITLE ---
root.title('Why did this start at the bottom of the desktop stacking order?') # Pass a string to set the windows title...
title = root.title() #...then call the method with 0 arguments to get the current title.


# --- CHANGING WINDOW SIZE AND LOCATION ---
#In Tkinter, position and size of a window is determined by geometry, the specification
#for which is:
#
# widthxheight+/-x+/-y

#To change size and pos. of window, use 'geometry()' method:
root.geometry('600x400+50+50')

#Maybe you want to center the window on the screen.  One way to 
#implement that is as follows:

window_width = 640
window_height = 480

#get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#finally, build the window's geometry based on the info we calculated:
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# ---RESIZING BEHAVIOR---
#By default, tkinter windows are resizable; you have explicity prevent this if
#you don't want the user to resize the window, as follows:

#root.resizable(False, False)

#on the other hand, if the window IS resizable, you can specify 
#it's minimum and maximum sizes using the 'minsize()' and 'maxsize()' methods.
root.minsize(int(screen_width/8), int(screen_height/8))
root.maxsize(int(screen_width/2), int(screen_height/2))

# --- TRANSPARENCY ---
#You can also make a window have a degree of transparency by setting it's alpha \
#channel ranging from 0.0 (fully transparent) to 1.0 (fullly opaque)

root.attributes('-alpha',0.5)


# --- WINDOW STACKING ORDER ---
# Stack order: order of windows placed on the screen from bottom to top.  The closer
# window is on the TOP of the stack, and it overlaps the one lower.
# To ensure that a window is always at the top of the stacking order, you can use the
# -topmost attribute like this:
root.attributes('-topmost', 1)

# Then to move a window up or down of the stack, you can use the lift() and lower()
# methods:

root.lift()
# root.lift(<name of another window that isn't root>)

root.lower()
# root.lower(<name of another window that isn't root>)



# ---CHANGING THE DEFAULT ICON---
# using 'iconbitmap()' you can select a '.ico' file to set the window icon.
root.iconbitmap('./assets/test.ico')
        
root.mainloop()

"""

"""
