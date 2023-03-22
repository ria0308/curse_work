from abc import ABC, abstractmethod
import numpy as np
import time


# class which represent system equations (linear) for splines
class SystemEquations(ABC):

    @abstractmethod
    def __matrix_solve(self):
        pass

    @abstractmethod
    def steps_output(self):
        pass


# class for doing cubic interpolation

class SystemEquationsForCubic(ABC):
    def __init__(self, lst_of_dots):
        self.__num_splines = len(lst_of_dots.lst) - 1
        # statistic
        self.__iterations = (self.__num_splines * 4) * ((self.__num_splines + 1) * 4)
        self.__operations = (self.__num_splines * 4) * ((self.__num_splines + 1) * 4) * 2
        self.__time = time.time()

        # matrix of coefficients
        self.__coefficients_x = [[0 for i in range(self.__num_splines * 4)] for j in range(self.__num_splines * 4)]
        self.__coefficients_y = [0 for i in range(self.__num_splines * 4)]

        # equations
        self.__first_equation(lst_of_dots.lst)
        self.__second_equation(lst_of_dots.lst)
        self.__third_equation(lst_of_dots.lst)
        self.__fourth_equation(lst_of_dots.lst)
        self.__extra_equation(lst_of_dots.lst)

        self.__result_of_solving = self.__matrix_solve().reshape(self.__num_splines, 4)

    @property
    def result_of_solving(self):
        return self.__result_of_solving

    @property
    def stats(self):
        return self.__iterations, self.__operations, self.__time

    @property
    def num_splines(self):
        return self.__num_splines

    def __matrix_solve(self):
        answer = np.linalg.solve(self.__coefficients_x, self.__coefficients_y)
        self.__time = time.time() - self.__time
        return answer

    def __first_equation(self, lst_of_dots):
        for i in range(self.__num_splines):
            self.__iterations += 1
            self.__coefficients_x[i][(i * 4)] = 1

            self.__coefficients_y[i] = lst_of_dots[i].y
            self.__operations += 6

    def __second_equation(self, lst_of_dots):
        for i in range(self.__num_splines):
            self.__iterations += 1

            self.__coefficients_x[self.__num_splines + i][(i * 4)] = 1
            self.__coefficients_x[self.__num_splines + i][(i * 4) + 1] = (lst_of_dots[i + 1].x - lst_of_dots[i].x)
            self.__coefficients_x[self.__num_splines + i][(i * 4) + 2] = pow((lst_of_dots[i + 1].x - lst_of_dots[i].x),
                                                                             2)
            self.__coefficients_x[self.__num_splines + i][(i * 4) + 3] = pow((lst_of_dots[i + 1].x - lst_of_dots[i].x),
                                                                             3)

            self.__coefficients_y[self.__num_splines + i] = lst_of_dots[i + 1].y

            self.__operations += 35

    def __third_equation(self, lst_of_dots):
        for i in range(self.__num_splines - 1):
            self.__iterations += 1
            # self.__coefficients_x[2 * self.__num_splines + i][(i * 4)] = 0
            self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 1] = 1
            self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 2] = 2 * (lst_of_dots[i + 1].x - lst_of_dots[i].x)
            self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 3] = 3 * pow(
                (lst_of_dots[i + 1].x - lst_of_dots[i].x), 2)

            # self.__coefficients_x[2 * self.__num_splines + i][i * 4] = 0
            self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 5] = -1
            # self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 6] = 0
            # self.__coefficients_x[2 * self.__num_splines + i][i * 4 + 7] = 0

            # self.__coefficients_y[2 * self.__num_splines + i] = 0

            self.__operations += 25

    def __fourth_equation(self, lst_of_dots):
        for i in range(self.__num_splines - 1):
            self.__iterations += 1
            # self.__coefficients_x[3 * self.__num_splines + i][(i * 4)] = 0
            # self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 1] = 0
            self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 2] = 2
            self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 3] = 6 * (lst_of_dots[i + 1].x - lst_of_dots[i].x)

            # self.__coefficients_x[3 * self.__num_splines + i][i * 4] = 0
            # self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 5] = 0
            self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 6] = - 2
            # self.__coefficients_x[3 * self.__num_splines + i][i * 4 + 7] = 0

            # self.__coefficients_y[3 * self.__num_splines + i] = 0

            self.__operations += 14

    def __extra_equation(self, lst_of_dots):
        self.__iterations += 1
        # self.__coefficients_x[3 * self.__num_splines - 1][0] = 0
        # self.__coefficients_x[3 * self.__num_splines - 1][1] = 0
        self.__coefficients_x[3 * self.__num_splines - 1][2] = 2
        # self.__coefficients_x[3 * self.__num_splines - 1][3] = 0

        self.__coefficients_y[3 * self.__num_splines - 1] = 0

        # self.__coefficients_x[4 * self.__num_splines - 1][(self.__num_splines - 1) * 4] = 0
        # self.__coefficients_x[4 * self.__num_splines - 1][(self.__num_splines - 1) * 4 + 1] = 0
        self.__coefficients_x[4 * self.__num_splines - 1][(self.__num_splines - 1) * 4 + 2] = 2
        self.__coefficients_x[4 * self.__num_splines - 1][(self.__num_splines - 1) * 4 + 3] = 6 * (
                    lst_of_dots[self.__num_splines].x - lst_of_dots[self.__num_splines - 1].x)

        # self.__coefficients_y[4 * self.__num_splines - 1] = 0

        self.__operations += 24

    def steps_output(self):
        text = "So, we will have cubic spline in format y = a + b(x-x0) + c(x-x0)^2 + d(x-x0)^3\n" \
               "by doing some math we will have this little matrix:\n"
        for i in range(self.__num_splines * 4):
            text += str(self.__coefficients_x[i]) + "  "
            text += "  " + str(self.__coefficients_y[i]) + "\n"

        text += "Now we solve this matrix using numpy and here is our results\n"
        for i in range(self.__num_splines):
            text += str(self.__result_of_solving[i]) + "\n"

        return text


# class for doing quadratic interpolation

class SystemEquationsForSquared(ABC):
    def __init__(self, lst_of_dots):
        self.__num_splines = len(lst_of_dots.lst) - 1
        # matrix initialize
        self.__coefficients_x = [[0 for i in range(self.__num_splines * 3)] for j in range(self.__num_splines * 3)]
        self.__coefficients_y = [0 for i in range(self.__num_splines * 3)]

        # statistic
        self.__iterations = (self.__num_splines * 3) * ((self.__num_splines + 1) * 3)
        self.__operations = (self.__num_splines * 3) * ((self.__num_splines + 1) * 3) * 2
        self.__time = time.time()

        # equations
        self.__first_equation(lst_of_dots.lst)
        self.__second_equation(lst_of_dots.lst)
        self.__third_equation(lst_of_dots.lst)
        self.__extra_equation(lst_of_dots.lst)

        self.__result_of_solving = self.__matrix_solve().reshape(self.__num_splines, 3)

    @property
    def result_of_solving(self):
        return self.__result_of_solving

    @property
    def num_splines(self):
        return self.__num_splines

    @property
    def stats(self):
        return self.__iterations, self.__operations, self.__time

    def __matrix_solve(self):
        answer = np.linalg.solve(self.__coefficients_x, self.__coefficients_y)
        self.__time = time.time() - self.__time
        return answer

    def __first_equation(self, lst_of_dots):
        for i in range(self.__num_splines):
            self.__iterations += 1
            self.__coefficients_x[i][(i * 3)] = 1

            self.__coefficients_y[i] = lst_of_dots[i].y

            self.__operations += 7

    def __second_equation(self, lst_of_dots):
        for i in range(self.__num_splines):
            self.__iterations += 1
            self.__coefficients_x[self.__num_splines + i][(i * 3)] = 1
            self.__coefficients_x[self.__num_splines + i][(i * 3) + 1] = (lst_of_dots[i + 1].x - lst_of_dots[i].x)
            self.__coefficients_x[self.__num_splines + i][(i * 3) + 2] = pow((lst_of_dots[i + 1].x - lst_of_dots[i].x),
                                                                             2)

            self.__coefficients_y[self.__num_splines + i] = lst_of_dots[i + 1].y

            self.__operations += 24

    def __third_equation(self, lst_of_dots):
        for i in range(self.__num_splines - 1):
            self.__iterations += 1
            # self.__coefficients_x[2 * self.__num_splines + i][(i * 3)] = 0
            self.__coefficients_x[2 * self.__num_splines + i][i * 3 + 1] = 1
            self.__coefficients_x[2 * self.__num_splines + i][i * 3 + 2] = 2 * (lst_of_dots[i + 1].x - lst_of_dots[i].x)

            # self.__coefficients_x[2 * self.__num_splines + i][i * 3 + 3] = 0
            self.__coefficients_x[2 * self.__num_splines + i][i * 3 + 4] = - 1
            # self.__coefficients_x[2 * self.__num_splines + i][i * 3 + 5] = 0

            # self.__coefficients_y[2 * self.__num_splines + i] = 0

            self.__operations += 18

    def __extra_equation(self, lst_of_dots):
        self.__iterations += 1
        # self.__coefficients_x[3 * self.__num_splines - 1][0] = 0
        self.__coefficients_x[3 * self.__num_splines - 1][1] = 1
        self.__coefficients_x[3 * self.__num_splines - 1][2] = 2 * (lst_of_dots[0].x - lst_of_dots[1].x)

        # self.__coefficients_y[3 * self.__num_splines - 1] = 0

        self.__operations += 10

    def steps_output(self):
        text = "So, we will have cubic spline in format y = a + b(x-x0) + c(x-x0)^2 \n" \
               "by doing some math we will have this little matrix:\n"
        for i in range(self.__num_splines * 3):
            text += str(self.__coefficients_x[i]) + "  "
            text += "  " + str(self.__coefficients_y[i]) + "\n"

        text += "Now we solve this matrix using numpy and here is our results\n"
        for i in range(self.__num_splines):
            text += str(self.__result_of_solving[i]) + "\n"

        return text
