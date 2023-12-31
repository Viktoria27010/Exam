import numpy as np


class Triangle:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def square(self, a=None, b=None, c=None):
        if a is None or b is None or c is None:
            if self.a is not None and self.b is not None and self.c is not None:
                a = self.a
                b = self.b
                c = self.c
            else:
                print("Мало данных")
                return

        s = (a + b + c) / 2
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
