import tkinter as tk
from interface.class_input_frame import InputFrame
from interface.class_result_frame import ResultFrame
from interface.class_extra_frame import ExtraFrame


#Here is class for main window

class MainForm(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Interpolation")
        self.wm_minsize(700, 500)
        self.wm_geometry('1000x700')
        self['background'] = '#EBEBEB'
        self.__input_frame = InputFrame(self, controller)
        self.__result_frame = ResultFrame(self)
        self.__extra_frame = ExtraFrame(self, controller)
        self.put_parts()

    @property
    def input_frame(self):
        return self.__input_frame

    @property
    def result_frame(self):
        return self.__result_frame

    @property
    def extra_frame(self):
        return self.__extra_frame

    def put_parts(self):
        self.input_frame.place(relx=0, rely=0, relwidth=0.4, relheight=0.5)
        self.result_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)
        self.extra_frame.place(relx=0, rely=0.5, relwidth=0.4, relheight=0.5)


