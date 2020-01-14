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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lines, = [ax.plot([], [], [], lw=0)]
points, = [ax.plot([], [], [], 'o', c='#ff7f0e', markersize=7,
                   markerfacecolor='None', markeredgewidth=0.5)]
ax.plot(x, y, z, c='teal', lw=0.5)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-1, 1)
ax.set_axis_off()

anim.AnimPlot3D(fig, ax, lines, points, x, y, z, plot_speed=5,
                rotation_speed=0.36, p_num=1)
plt.show()
