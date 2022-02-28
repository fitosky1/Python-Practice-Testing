"""
day 12
GUI tkinter
Each GUI is a class
"""
#
# Imports
import tkinter as tk

#
# class hello1(object):
#     """docstring for hello1."""
#
#     def __init__(self, arg_text):
#         self.root = tk.Tk()
#         self.w = tk.Label(
#             self.root, text=arg_text, width=30, height=30
#         )  # for label  height=30
#         self.w.pack()  # padx=100, pady=10
#         self.root.mainloop()
#         # self.root.winfo_screenwidth(600)
#         # self.root.winfo_screenheight(400)
#         # self.height = 20
#         # self.root.

# hello1("Holanda q talca")


def Print_Out(arg_1):
    print(arg_1)


class guitest(object):
    """docstring for guitest."""

    def __init__(self, arg_t1, arg_t2):
        self.root = tk.Tk()
        self.root.title("Window Title")
        self.w1 = tk.Label(
            self.root,
            text=arg_t1,
            bg="red",
            width=30,
            height=10,
            font=("Helvetica", 30),
        )
        self.w2 = tk.Label(
            self.root, text=arg_t2, bg="blue", width=40, height=20, padx=20
        )
        self.w3 = tk.Label(
            self.root,
            text="Text 3\n2Line\n3Line",
            bg="green",
            width=35,
            height=15,
            anchor="e",
            justify="right",
            font=("Times", 30),
        )
        self.button1 = tk.Button(
            self.root, text="close me", command=quit
        )  # Or self.root.destroy or, lambda: Print_Out("Hello World!!") to execute a external function
        self.button1.pack(side="top")
        self.w1.pack(side="left")  # padx=100, pady=10
        self.w2.pack()  # padx=100, pady=10
        self.w3.pack()  # padx=100, pady=10
        self.root.mainloop()


guitest("hola", "hallo")
