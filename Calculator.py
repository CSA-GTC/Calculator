'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

#Gregory Clarke
#Advanced Computer Programming
#11/12/2018

from tkinter import *
from tkinter import ttk
import tkinter as tk

class App:

    def __init__(self, master):
        self.expression = "" #What the numbers are added to after being clicked on
        self.content = tk.Frame(root, bg="light blue") #the frame that each widget is a part of
        self.menubar = Menu(root)  # menubar
        self.filemenu = Menu(self.menubar, tearoff=0) #options in menu
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # creates option in menubar
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.filemenu.add_command(label="Previous Answers", command=self.file_read)

        self.menubar2 = Menu(root)  # second menu for "help"
        self.helpmenu = Menu(self.menubar2, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  # creates option in menubar
        self.helpmenu.add_command(label="About", command=self.new)  # option in help
        root.config(menu=self.menubar)

        self.show = StringVar() #displays the numbers being worked with
        self.name = ttk.Entry(self.content, textvariable=self.show, state="readonly")
        self.one = ttk.Button(self.content, text="1", command=lambda: self.press(1))
        self.two = ttk.Button(self.content, text="2", command=lambda: self.press(2))
        self.three = ttk.Button(self.content, text="3", command=lambda: self.press(3))
        self.four = ttk.Button(self.content, text="4", command=lambda: self.press(4))
        self.five = ttk.Button(self.content, text="5", command=lambda: self.press(5))
        self.six = ttk.Button(self.content, text="6", command=lambda: self.press(6))
        self.seven = ttk.Button(self.content, text="7", command=lambda: self.press(7))
        self.eight = ttk.Button(self.content, text="8", command=lambda: self.press(8))
        self.nine = ttk.Button(self.content, text="9", command=lambda: self.press(9))
        self.zero = ttk.Button(self.content, text="0", command=lambda: self.press(0))
        self.multi = ttk.Button(self.content, text="*", command=lambda: self.press("*"))
        self.div = ttk.Button(self.content, text="/", command=lambda: self.press("/"))
        self.sub = ttk.Button(self.content, text="-", command=lambda: self.press("-"))
        self.add = ttk.Button(self.content, text="+", command=lambda: self.press("+"))
        self.clear = ttk.Button(self.content, text="Clear", command=self.clear)
        self.dec = ttk.Button(self.content, text=".", command=lambda: self.press("."))
        self.neg = ttk.Button(self.content, text="(-)", command=lambda: self.press("-"))
        self.enter = ttk.Button(self.content, text="=", command=self.equalpress)

        self.content.grid(column=0, row=0, sticky="nsew", padx=(12,12), pady=(12,12))
        self.name.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=(12,12), pady=(12,12))
        self.one.grid(column=0, row=1, sticky="nsew", padx=(12,12), pady=(12,12))
        self.two.grid(column=1, row=1, sticky="nsew", padx=(12,12), pady=(12,12))
        self.three.grid(column=2, row=1, sticky="nsew", padx=(12,12), pady=(12,12))
        self.div.grid(column=3, row=1, padx=(12,12), pady=(12,12))
        self.four.grid(column=0, row=2, padx=(12,12), pady=(12,12))
        self.five.grid(column=1, row=2, padx=(12,12), pady=(12,12))
        self.six.grid(column=2, row=2, padx=(12,12), pady=(12,12))
        self.multi.grid(column=3, row=2, padx=(12,12), pady=(12,12))
        self.seven.grid(column=0, row=3, padx=(12,12), pady=(12,12))
        self.eight.grid(column=1, row=3, padx=(12,12), pady=(12,12))
        self.nine.grid(column=2, row=3, padx=(12,12), pady=(12,12))
        self.sub.grid(column=3, row=3, padx=(12,12), pady=(12,12))
        self.zero.grid(column=0, row=4, padx=(12,12), pady=(12,12))
        self.dec.grid(column=1, row=4, padx=(12,12), pady=(12,12))
        self.neg.grid(column=2, row=4, padx=(12,12), pady=(12,12))
        self.add.grid(column=3, row=4, padx=(12,12), pady=(12,12))
        self.clear.grid(column=3, row=0, padx=(12,12), pady=(12,12))
        self.enter.grid(column=2, row=0)

        root.columnconfigure(0, weight=1)  # weight for rows and columns
        root.rowconfigure(0, weight=1)
        root.minsize(435, 285)

    def press(self, num):
        # concatenation of string
        self.expression = self.expression + str(num)

        # update the expression by using set method
        self.show.set(self.expression)

    def equalpress(self): #evaluates the string with all the numbers to get an answer

        try:
            self.total = str(eval(self.expression))
            self.show.set(self.total)
            self.expression = ""
            self.file_append() #adds number to a file

        except:
            self.show.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.show.set("")

    def file_append(self):
        with open("calc_log", "a") as file:
            file.write(self.total+"\n")

    def file_read(self): # reads through file to get previous answers
        try:
            self.text = []
            with open("calc_log", "r") as file:

                for line in file:
                    self.text.append(line)

            for x in self.text:
                x.replace("\n", "")
            self.answers()

        except:
            self.error()

    def answers(self): # top level that displays answers
        top = Toplevel(root, padx=15, pady=15)
        top.title("Answers")
        t = StringVar()
        nums=""
        if self.text == []:
            t.set("There are no previous answers!")

        elif self.text != []:
            for x in self.text:
                nums += x
        t.set(nums)

        msg = Message(top, textvariable=t, width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)

    def error(self): #backup error message
        top = Toplevel(root, padx=15, pady=15)
        top.title("Error")
        msg = Message(top, text="Something went wrong!", width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)

    def new(self):  # makes new top level for about program
        top = Toplevel(root, padx=15, pady=15)
        top.title("About")
        msg = Message(top, text="Calculator\nVersion 1.0\nGregory Clarke", width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)


root = Tk()
root.config(background="light green")
root.resizable(width=False, height=False)
app = App(root)
root.title("Calculator")
root.mainloop()
root.destroy()
