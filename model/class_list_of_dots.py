from model.class_dot import Dot

# this class store in self all dots


class ListOfDots:
    def __init__(self):
        self.__lst = []

    @property
    def lst(self):
        return self.__lst

    def validate(self, number):
        try:
            num = float(number)
        except ValueError:
            return 0
        except OverflowError:
            return 0
        else:
            return 1

    def add_dot(self, x, y):
        if not(self.validate(x) and self.validate(y)):
            return "mistake, input is invalid, maybe you have inputed some letters or number which is more then 10^50"
        elif sum(1 for item in self.__lst if float(x) == item.x) > 0:
            return "mistake, you can`t add two dots with same x"
        self.__lst.append(Dot(float(x), float(y)))
        self.__lst = sorted(self.__lst, key=lambda a: a.x)
        return "success"

    def dots_for_output(self):
        text = 'Here\'s your dots\n'
        for dot in self.__lst:
            text += f'x = {dot.x}   y = {dot.y}\n'
        return text

    def clear_list(self):
        self.__lst = []





