import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#part of window for showing results

class ResultFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self['background'] = '#BACDDC'

        self.__text_widget = tk.Text(self, width=70, height=10, state='disabled')
        self.__graph_wid, self.__graph = plt.subplots()

        self.put_widgets()

    def put_widgets(self, graphic_data=[[], [], [], []], result_text='Here will be your polynoms stored'):
        # polynoms

        self.__text_widget.config(state='normal')
        self.__text_widget.delete(1.0, tk.END)
        self.__text_widget.insert(tk.END, result_text)
        self.__text_widget.config(state='normal')
        self.__text_widget.place(relx=0.2, rely=0.05, relheight=0.3, relwidth=0.6)

        # graph
        self.__graph.clear()
        for i in range(len(graphic_data[0])):
            self.__graph.plot(graphic_data[0][i], graphic_data[1][i])
        self.__graph.scatter(graphic_data[-2], graphic_data[-1])
        canvas = FigureCanvasTkAgg(self.__graph_wid, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(rely=0.4, relheight=0.5, relx=0.1, relwidth=0.8)


