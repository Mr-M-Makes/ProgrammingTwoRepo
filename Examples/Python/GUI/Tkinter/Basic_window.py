import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

#window class
class basic_window(tk.Tk):
    def __init__(self,window_name):
        super().__init__()
        self.title(window_name)
        self._cells = {}

window = basic_window("Basic Window Template")
window.mainloop()