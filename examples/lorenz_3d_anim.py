import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import animplotlib as anim

sigma = 10
rho = 28
beta = 8 / 3
x0 = [0, 1, 15]
t = np.linspace(0.01, 50, 10000)


def lorenz(x_var, t):
    x, y, z = x_var
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]


x_solve = odeint(lorenz, x0, t)
x = x_solve[:, 0]
y = x_solve[:, 1]
z = x_solve[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

(lines,) = ax.plot([], [], [], lw=0.5)
(points,) = ax.plot([], [], [], "ro", markersize=4)
ax.set_title("Lorenz Attractor")
ax.set_axis_off()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))

anim.AnimPlot3D(fig, ax, lines, points, x, y, z, plot_speed=1, rotation_speed=0.1)
