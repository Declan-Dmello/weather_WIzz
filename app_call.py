from tkinter import *

import testing_ground


def open_b_toplevel_window():
    toplevel_window = Toplevel(testing_ground.root)
    toplevel_window.title('Focusing on Text Entery')
    toplevel_window.geometry('270x100')
    label = Label(toplevel_window, text='Enter Text Now')
    label.pack()
    text_entry = Text(toplevel_window, width=10, height=3)
    text_entry.focus_set()
    text_entry.pack()
    toplevel_window.attributes('-topmost', True)