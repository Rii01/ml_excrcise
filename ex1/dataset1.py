import numpy as np
import matplotlib.pyplot as plt

def true_function(X):
    y = np.sin(np.pi * X * 0.8) * 10
    return y

height = np.array([])


x = np.arange(-1, 1, 0.1)
y = true_function(x)
plt.plot(x, y)
plt.show()
fig = plt.figure()
fig.savefig('ex1_1.png')
