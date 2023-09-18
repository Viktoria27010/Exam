import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.01)
a = ((x**2+1)*(np.exp(-abs(x)/10)))
b = (1+np.tan(1/(1+(np.sin(x))**2)))
y = np.log(a)/np.log(b)
plt.plot(x, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
