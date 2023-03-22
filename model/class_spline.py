from abc import ABC, abstractmethod
import numpy as np


# class for storage spline
class Spline(ABC):
    @abstractmethod
    def spline_nice_view(self):
        pass

    @abstractmethod
    def spline_for_graph(self):
        pass


# class for storage cubic spline
class CubicSpline(ABC):
    def __init__(self, dot0, dot1, coeffs):
        self.__dot0 = dot0
        self.__dot1 = dot1
        self.__coeffs = coeffs

    @property
    def dot0(self):
        return self.__dot0

    @property
    def dot1(self):
        return self.__dot1

    @property
    def coeffs(self):
        return self.__coeffs

    def spline_nice_view(self):
        view = f'y = {round(self.__coeffs[0], 3)} + ({round(self.__coeffs[1], 3)})*(x - {round(self.__dot0.x, 3)}) + ' \
               f'({round(self.__coeffs[2], 3)}*(x - {round(self.__dot0.x, 3)})^2 + ({round(self.__coeffs[3], 3)})*(x - {round(self.__dot0.x, 3)})^3 ,\n ' \
               f'{self.__dot0.x} < x < {self.dot1.x}\n'
        return view

    def spline_for_graph(self):
        x = np.linspace(self.__dot0.x, self.__dot1.x, 1000)
        y = self.__coeffs[0] + self.coeffs[1] * (x - self.__dot0.x) + self.coeffs[2] * (x - self.__dot0.x) ** 2 + \
            self.coeffs[3] * (x - self.__dot0.x) ** 3
        return x, y


# class for storage quadratic spline
class SquaredSpline(ABC):
    def __init__(self, dot0, dot1, coeffs):
        self.__dot0 = dot0
        self.__dot1 = dot1
        self.__coeffs = coeffs

    @property
    def dot0(self):
        return self.__dot0

    @property
    def dot1(self):
        return self.__dot1

    @property
    def coeffs(self):
        return self.__coeffs

    def spline_nice_view(self):
        view = f'y = {round(self.__coeffs[0], 3)} + ({round(self.__coeffs[1], 3)})*(x - {round(self.__dot0.x, 3)}) + ' \
               f'({round(self.__coeffs[2], 3)}*(x - {round(self.__dot0.x, 3)})^2 ,\n ' \
               f'{self.__dot0.x} < x < {self.dot1.x}\n'
        return view

    def spline_for_graph(self):
        x = np.linspace(self.__dot0.x, self.__dot1.x, 1000)
        y = self.__coeffs[0] + self.coeffs[1] * (x - self.__dot0.x) + self.coeffs[2] * (x - self.__dot0.x) ** 2
        return x, y
