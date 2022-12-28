import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, axes = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = axes.plot(x, np.sin(x))
axes.grid()

def animate(i):
    line.set_xdata(x)
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,

ani=animation.FuncAnimation(fig,animate,interval=20)
plt.show()