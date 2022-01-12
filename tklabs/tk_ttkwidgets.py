"""
Based on a tutorial at:

https://www.pythontutorial.net/tkinter/tkinter-ttk/
"""

import tkinter as tk # These are the classic Tk themed widgets.

from tkinter import ttk # These are the "new" Tk themed widgets; recommend using these exclusively in production apps.

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()

'''
For future reference:
The ttk widgets
The following ttk widgets replace the Tkinkter widgets with the same names:

Button
Checkbutton
Entry
Frame
Label
LabelFrame
Menubutton
PanedWindow
Radiobutton
Scale
Scrollbar
Spinbox
And the following widgets are new and specific to ttk:

Combobox
Notebook
Progressbar
Separator
Sizegrip
Treeview
'''

'''
SUMMARY
Tkinter has both classic and themed widgets.  Tk themed widgets are also known as ttk widgets.
The 'tkinter.ttk' module contains all the ttk widgets.
DO use the ttk widgets whenever they're available.
'''