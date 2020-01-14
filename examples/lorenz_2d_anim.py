import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import animplotlib as anim

plt.style.use('dark_background')

sigma = 10
rho = 28
beta = 8/3
x0 = [0, 1, 15]
t = np.linspace(0.01, 100, 10000)


def lorenz(x, t):
    x1 = x[0]
    y = x[1]
    z = x[2]

    dx_dt = sigma * (y - x1)
    dy_dt = x1 * (rho - z) - y
    dz_dt = x1 * y - beta * z

    return [dx_dt, dy_dt, dz_dt]


x_solve = odeint(lorenz, x0, t)

x = x_solve[:, 0]
y = x_solve[:, 1]
z = x_solve[:, 2]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 3))

line1, = ax1.plot([], [], c='yellow', lw=0.15)
line2, = ax2.plot([], [], c='teal', lw=0.15)
line3, = ax3.plot([], [], c='orange', lw=0.15)

xlim = (-25, 25)
ylim = (-25, 25)
zlim = (0, 45)

ax1.set_xlim(xlim)
ax1.set_ylim(ylim)
ax1.set_axis_off()

ax2.set_xlim(xlim)
ax2.set_ylim(zlim)
ax2.set_axis_off()

ax3.set_xlim(ylim)
ax3.set_ylim(zlim)
ax3.set_axis_off()

anim.AnimPlot(fig, line1, x, y, plot_speed=4)
anim.AnimPlot(fig, line2, x, z, plot_speed=4)
anim.AnimPlot(fig, line3, y, z, plot_speed=4)
plt.show()
