# this class store in self all splines

class SplineList:
    def __init__(self):
        self.__splines_lst = []

    @property
    def spline_list(self):
        return self.__splines_lst

    @spline_list.setter
    def spline_list(self, value):
        self.__splines_lst = value

    def splines_output(self):
        text = 'Here is all splines\n'
        for item in self.__splines_lst:
            text += item.spline_nice_view() + "\n"
        return text

    def splines_for_graph(self):
        x = []
        y = []
        dotsx = [self.__splines_lst[0].dot0.x]
        dotsy = [self.__splines_lst[0].dot0.y]
        for item in self.__splines_lst:
            x.append(item.spline_for_graph()[0])
            y.append(item.spline_for_graph()[1])
            dotsx.append(item.dot1.x)
            dotsy.append(item.dot1.y)
        return x, y, dotsx, dotsy
