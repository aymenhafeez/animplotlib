import testanim as anim
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

x = np.linspace(-7, 7, 5000)
y, z = sc.fresnel(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lines, = ax.plot([], [], [], lw=1)
points, = ax.plot([], [], [], 'ro', markersize=5)

ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))
ax.set_title("Animated 3D Fresnel Plot")

anim.AnimPlot3D(fig, ax, [lines], [points], x, y, z, plot_speed=35)
