import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def true_function(X):
    y = np.sin(np.pi * X * 0.8) * 10
    return y

height = np.array([])

np.random.seed(0)
xdot = np.random.uniform(-1, 1, size=20)
ydot = true_function(xdot)
pd = pd.DataFrame({"観測点": xdot, "真値": ydot})
x = np.arange(-1, 1, 0.1)
y = true_function(x)
plt.plot(x, y, label="true value")
plt.scatter(xdot, ydot, c="pink",)
plt.show()
fig = plt.figure()
fig.savefig('./Dataset/ex1_2/ex1.2.png')


