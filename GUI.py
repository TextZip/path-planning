import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy.core.fromnumeric import repeat

# data = np.random.rand(10, 10) * 20
def animate(i):
    data = np.random.rand(10, 10) * 20
    # global data
    cmap = colors.ListedColormap(['red', 'blue','green','white'])
    bounds = [0,5,10,15,20]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    global fig
    global ax
    ax.clear()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10.5, 1))
    ax.set_yticks(np.arange(-.5, 10.5, 1))
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

# data = np.array([[2,2,2,2,2],[7,7,7,7,7],[12,12,12,12,12],[17,17,17,17,17],[2,7,12,17,-5]])
# print(data)
fig, ax = plt.subplots()


def onClick(event):
    anim.event_source.stop()
fig.canvas.mpl_connect('button_press_event', onClick)
anim = FuncAnimation(fig, animate)
plt.show()