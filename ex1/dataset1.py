import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, -1, 0.1, 1])
def true_function(X):
    y = np.sin(np.pi * X * 0.8) * 10
    return y
print(true_function(x[0]))
height = np.array([])

for i in range(len(x)):
    height = np.append(height, true_function(x[i]))
print(height)
size = np.sort(x)
print(size)


plt.plot(size, height)
plt.show()
plt.xlim(-1, 1)