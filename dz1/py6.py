import numpy as np
import matplotlib.pyplot as plt
x_1 = np.arange(-2, 2.01, 0.001)
a = 100
b = 0.5
c = 3
y_1 = np.array([])
y = np.array([])
for x in x_1:
    for i in range(a):
        y = np.append(y, np.cos(np.pi*x*c**i)*b**i)
    y_2 = np.sum(y)
    y_1 = np.append(y_1, y_2)
    y = np.array([])

plt.plot(x_1, y_1)
plt.axis('equal')
plt.grid(True)
plt.show()
