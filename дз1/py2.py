import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.01)
plt.plot(x, x*x - x - 6)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$y(x) = x*x - x - 6$')
plt.grid(True)
plt.show()
