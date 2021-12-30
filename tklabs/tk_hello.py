"""
This file produced based on examples in:

https://www.pythontutorial.net/tkinter/tkinter-hello-world/
"""

import tkinter as tk #Import tkinter module as tk to the program


root = tk.Tk() # Create instance of tk.Tk class that will create the app window



message = tk.Label(root, text="Hello, World!") # Create a "label" widget, and place it within the root window
message.pack() # This positions the Label on the main window.  (widget will exist, yet be invisible if this is not called; more on that later)



try: 
    from ctypes import windll #Used for optional Windows compatibility features; sometimes tkinter apps are blurry due to how Windows works.  
#Importing the ctypes library allows us to set process DPI awareness to correct this.
    windll.shcore.SetProcessDpiAwareness(1) # fixes potential DPI issues on Windows machines.

finally:
    root.mainloop() # call mainloop() method of the main window object:

# without calling mainloop(), the window will appear and disappear immediately; it will
# be so fast you won't see it.

# Typically, root.mainloop() is the LAST line in a tkinter program, after creating the widgets.





