import numpy as np
import matplotlib.pyplot as plt
import animplotlib as anim

n = 1000
phi = np.linspace(0, 2 * np.pi, n)
x = np.sin(phi) + 2 * np.sin(2 * phi)
y = np.cos(phi) - 2 * np.cos(2 * phi)
z = -np.sin(3 * phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lines, = ax.plot([], [], [], lw=0)
points, = ax.plot([], [], [], 'o', markersize=10, markerfacecolor='None',)
ax.plot(x, y, z, c='lightblue')

ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))
ax.set_axis_off()

anim.AnimPlot3D(fig, ax, [lines], [points], x, y, z, plot_speed=1,
                rotation_speed=0.36, p_num=1)
