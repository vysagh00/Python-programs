import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi,0.1)

y = np.sin(x)
plt.plot(x,y)
plt.show()

y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.show()

y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("sine and cosine graph")
plt.legend(["sin","cos"])
plt.show()

