from tkinter import *
from centerlib import makecenter

root = Tk()
root.title("Hello Python Tkinter")
Label(root, text="Xin chào! Tui là Tkinter", justify=CENTER, relief=SUNKEN).pack(pady=50)
root.resizable(width=True, height=True)
root.minsize(width=500, height=300)
makecenter(root)
root.mainloop()
