from model.class_list_of_dots import ListOfDots
from model.class_system_equations import *
from model.class_list_of_splines import SplineList
from model.class_spline import *
from interface.class_main_window import MainForm
import pickle

from tkinter import messagebox

import tkinter as tk


# here is class which controls all done things

class Controler:
    def __init__(self):
        self.__list_of_dots = ListOfDots()
        self.__list_of_splines = SplineList()
        self.__system_equations = []
        self.__result_view = ''

        self.__main_form = MainForm(self)

    @property
    def main_form(self):
        return self.__main_form

    def interpolate(self, method):
        if len(self.__list_of_dots.lst) < 2:
            self.show_error("Not enough dots")
        else:
            self.__list_of_splines.spline_list = []
            if method == 0:
                self.show_error('First of all, you should choose method')
            if method == 1:
                self.square_interpolate()
            if method == 2:
                self.cubic_interpolate()

    def square_interpolate(self):
        self.__system_equations = SystemEquationsForSquared(self.__list_of_dots)
        solved_system = self.__system_equations.result_of_solving
        for i in range(len(solved_system)):
            self.__list_of_splines.spline_list.append(
                SquaredSpline(self.__list_of_dots.lst[i], self.__list_of_dots.lst[i + 1], solved_system[i]))
        self.__result_view = self.__list_of_splines.splines_output()
        self.main_form.result_frame.put_widgets(self.__list_of_splines.splines_for_graph()[0:4],
                                                self.__result_view)
        self.main_form.extra_frame.put_widgets()

    def cubic_interpolate(self):
        self.__system_equations = SystemEquationsForCubic(self.__list_of_dots)
        solved_system = self.__system_equations.result_of_solving
        for i in range(len(solved_system)):
            self.__list_of_splines.spline_list.append(
                CubicSpline(self.__list_of_dots.lst[i], self.__list_of_dots.lst[i + 1], solved_system[i]))
        self.__result_view = self.__list_of_splines.splines_output()
        self.main_form.result_frame.put_widgets(self.__list_of_splines.splines_for_graph()[0:4],
                                                self.__result_view)
        self.main_form.extra_frame.put_widgets()

    def show_steps(self):
        if self.__system_equations == []:
            self.show_error("You haven`t done any interpolation, whats steps are you want?")
        else:
            text = "first of all, we have a dots list\n"
            text += self.__list_of_dots.dots_for_output()
            text += self.__system_equations.steps_output()
            text += self.__list_of_splines.splines_output()
            self.__main_form.extra_frame.put_widgets(text)

    def write_to_file(self):
        if self.__system_equations == []:
            self.show_error("You haven`t done any interpolation, whats are you going to write?")
        f = open("results.txt", 'a')
        f.write("here are your splines:\n")
        for spline in self.__list_of_splines.spline_list:
            f.write(spline.spline_nice_view() + "\n")
        f.close()


    def show_error(self, text):
        messagebox.showerror("Oops, something goes wrong", text)

    def add_dot(self, x, y):
        if self.__list_of_dots.add_dot(x, y) == 'success':
            if len(self.__list_of_dots.lst) > 100:
                self.show_error("You can`t add more then 100 dots")
            else:
                self.__main_form.input_frame.put_widgets(self.__list_of_dots.dots_for_output())
                self.__main_form.result_frame.put_widgets()
                self.__main_form.extra_frame.put_widgets()
                self.__system_equations = []
        else:
            self.show_error(self.__list_of_dots.add_dot(x, y))

    def remove_all_dots(self):
        self.__list_of_dots.clear_list()
        self.__system_equations = []
        self.__main_form.input_frame.put_widgets(self.__list_of_dots.dots_for_output())
        self.__main_form.extra_frame.put_widgets()
        self.__main_form.result_frame.put_widgets()

    def statistic(self):
        if self.__system_equations == []:
            self.show_error("You haven`t done any interpolation, what statistic do you want?")
        else:
            text = f'Interpolation: \n{self.__system_equations.stats[0]} iterations\n{self.__system_equations.stats[1]} operations \n{round(self.__system_equations.stats[2] * 1000, 5)} miliseconds'
            messagebox.showinfo("Statistic", text)


    def dots_dump(self):
        with open("binary.bin", "wb") as m:
            pickle.dump(self.__list_of_dots, m)

    def load(self):
        with open("binary.bin", "rb") as m:
            self.__list_of_dots = pickle.load( m)
        self.__main_form.input_frame.put_widgets(self.__list_of_dots.dots_for_output())
        self.__main_form.result_frame.put_widgets()
        self.__main_form.extra_frame.put_widgets()
        self.__system_equations = []