import tkinter as tk
from tkinter import *


# part of window for extra things - steps, filewriting, statistic
class ExtraFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.__steps = tk.Text(self, width=70, height=10, state='disabled')
        self.__controler = controller
        self.put_widgets()

    def put_widgets(self, steps="Here will be your steps:"):
        # button for showing steps
        def b_show_steps_click():
            self.__controler.show_steps()

        b_show_steps = Button(self, text="SHOW STEPS", command=b_show_steps_click)
        b_show_steps.place(relx=0.1, rely=0.85)

        # button for writing in file
        def b_write_to_file_click():
            self.__controler.write_to_file()

        b_write_to_file = Button(self, text="WRITE TO FILE", command=b_write_to_file_click)
        b_write_to_file.place(relx=0.4, rely=0.85)

        def b_statistic_click():
            self.__controler.statistic()

        b_statistic = Button(self, text="STATISTIC", command=b_statistic_click)
        b_statistic.place(relx=0.75, rely=0.85)

        # steps widget
        self.__steps.config(state='normal')
        self.__steps.delete(1.0, tk.END)
        self.__steps.insert(tk.END, steps)
        self.__steps.config(state='disabled')
        self.__steps.place(relx=0.1, rely=0.1, relheight=0.6, relwidth=0.8)

        def b_load_click():
            self.__controler.load()
        b_statistic = Button(self, text="LOAD", command=b_load_click)
        b_statistic.place(relx=0.75, rely=0.75)

        def b_dump_click():
            self.__controler.dots_dump()
        b_statistic = Button(self, text="WRITE DOTS", command=b_dump_click)
        b_statistic.place(relx=0.45, rely=0.75)