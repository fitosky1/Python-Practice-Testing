"""
day 12
GUI tkinter
Each GUI is a class
"""
#
# Imports
import tkinter as tk

"""
First GUI
"""


class SimpleInput:
    """docstring for SimpleInput."""

    def __init__(self):
        self.root = tk.Tk()
        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
        self.edit1 = tk.Entry(self.root, textvariable=self.input1)
        self.edit2 = tk.Entry(self.root, textvariable=self.input2)
        self.edit1.pack()
        self.edit2.pack()
        self.button1 = tk.Button(
            self.root, text="click me for result", command=lambda: self.operate()
        )  # lambda: self.operate()
        self.button1.pack()
        self.resultw = tk.Label(self.root, text="hola")  # self.operate()
        self.resultw.pack()
        self.root.mainloop()

    def operate(self):
        nr1 = self.edit1.get()
        nr2 = self.edit2.get()
        self.result = tk.StringVar()
        self.result = float(nr1) + float(nr2)
        self.resultw.config(text=self.result)
        # self.edit1.delete(0)
        self.edit1.config(textvariable=self.result)
        # self.edit1.insert(0, self.result)


SimpleInput()

"""
Seconf GUI
"""
# Simple click counter
# IS WORKING
# class Counter(object):
#     """docstring for ."""
#
#     def __init__(self):
#         self.root = tk.Tk()
#         self.value = 0
#         self.w = tk.Label(self.root, text="hola")
#         self.button1 = tk.Button(
#             self.root, text="click me", command=lambda: self.adding()
#         )
#         self.w.pack()
#         self.button1.pack()
#         self.root.mainloop()
#
#     def adding(self):
#         self.value += 1
#         self.w.config(text=self.value)
#
#
# # run the counter
# Counter()
