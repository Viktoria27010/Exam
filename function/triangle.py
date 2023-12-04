import numpy as np
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        s = (self.a + self.b + self.c) / 2
        area = np.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

def square(a, b, c):
        s = (a + b + c) / 2
        tr = np.sqrt(s * (s - a) * (s - b) * (s - c))
        return tr

