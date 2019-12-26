import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import animplotlib as anim

plt.style.use('dark_background')

n = 1000
phi = np.linspace(0, 2 * np.pi, n)
x = np.sin(phi) + 2 * np.sin(2 * phi)
y = np.cos(phi) - 2 * np.cos(2 * phi)
z = -np.sin(3 * phi)


def shape_data(x, y, z):
    data = np.array([x, y, z])
    data_transpose = np.array([data]).T
    data_plot = np.reshape(data_transpose, (1, n, 3), order='C')
    return data_plot


array = shape_data(x, y, z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lines, = [ax.plot([], [], [], lw=0.5, c=(0.5, 0.8, 0.75))]
points, = [ax.plot([], [], [], 'o', c='#ff7f0e', markersize=7,
                   markerfacecolor='None', markeredgewidth=0.75)]
ax.plot(x, y, z, lw=0.5, c=(0.5, 0.8, 0.75))

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-1, 1)
ax.set_axis_off()

anim.AnimPlot3D(fig, ax, lines, points, array, plot_speed=3,
                rotation_speed=0.36)
plt.show()
