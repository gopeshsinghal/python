import numpy as np
import matplotlib.pyplot as plt

"""
x = np.arange(0, 6*np.pi,0.1)
#y = np.sin(x)
y = np.cos(x)

plt.plot(x,y)
plt.show()
"""

x = np.arange(0, 3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)

plt.xlabel("x axis lebel")
plt.ylabel("y axis lebel")
plt.title("sin and cosine graph")
plt.legend(["sin", "cos"])

plt.show()
    