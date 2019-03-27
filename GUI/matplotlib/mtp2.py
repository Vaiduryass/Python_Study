import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = 0

line, = ax.plot([], [], lw=2)
xdata, ydata = [], []
ax.set_ylim(-1, 1)
def update_line(i):
    y = np.sin(x + i / 5)

    xdata.append(i)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.set_xlim(0, i+1)
    ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,


ani = FuncAnimation(fig, update_line, blit=True, interval=25, frames=1000)
plt.show()
