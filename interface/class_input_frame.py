from tkinter import *
import tkinter as tk


# Part of window where input is done
class InputFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # self['background'] = self.master['background']
        self['background'] = '#B111DC'

        self.__choose_method = tk.IntVar(self, 0)
        self.__controller = controller
        self.__dots_list = tk.Text(self, width=70, height=10, state='disabled')
        self.put_widgets()

    def put_widgets(self, dots_list="Here will be your dots stored"):
        e_input_x = tk.Entry(self, bg="white", fg="black", width=50)
        e_input_y = tk.Entry(self, bg="white", fg="black", width=50)
        e_input_x.place(relx=0.1, rely=0.2, relwidth=0.1)
        e_input_y.place(relx=0.1, rely=0.3, relwidth=0.1)

        tk.Label(self, text="x").place(relx=0.05, rely=0.2, relwidth=0.04)
        tk.Label(self, text="y").place(relx=0.05, rely=0.3, relwidth=0.04)

        def b_add_dot_click():
            self.__controller.add_dot(e_input_x.get(), e_input_y.get())

        b_add_dot = Button(self, text="+", command=b_add_dot_click)
        b_add_dot.place(relx=0.4, rely=0.50)

        def b_clear_list_click():
            self.__controller.remove_all_dots()

        b_add_dot = Button(self, text="clear all", command=b_clear_list_click)
        b_add_dot.place(relx=0.5, rely=0.50)

        tk.Radiobutton(self, text='Interpolation by quadratic splines', variable=self.__choose_method, value=1).place(
            relx=0.1, rely=0.7)
        tk.Radiobutton(self, text='Interpolation by cubic splines', variable=self.__choose_method, value=2).place(
            relx=0.1, rely=0.75)

        def b_interpolate_click():
            self.__controller.interpolate(self.__choose_method.get())

        b_interpolate = Button(self, text="INTERPOLATE", command=b_interpolate_click)
        b_interpolate.place(relx=0.4, rely=0.90)

        self.__dots_list.config(state='normal')
        self.__dots_list.delete(1.0, tk.END)
        self.__dots_list.insert(tk.END, dots_list)
        self.__dots_list.config(state='disabled')
        self.__dots_list.place(relx=0.3, rely=0.1, relheight=0.4, relwidth=0.5)
