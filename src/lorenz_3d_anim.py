import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import animplotlib as anim

plt.style.use('dark_background')

sigma = 10
rho = 28
beta = 8/3
x0 = [0, 1, 20]
t_s, t_m = 0, 150
t = np.linspace(t_s, t_m, 50000)


def lorenz(x_var, t):
    x = x_var[0]
    y = x_var[1]
    z = x_var[2]

    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return [dx_dt, dy_dt, dz_dt]


x_solve = np.array([odeint(lorenz, x0, t)])

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

lines, = [ax.plot([], [], [], lw=0.25)]
points, = [ax.plot([], [], [], 'o', markerfacecolor='None', markersize=7,
                   markeredgewidth=0.25)]

ax.set_xlim((-15, 15))
ax.set_ylim((-20, 20))
ax.set_zlim((0, 40))
ax.set_axis_off()

anim.AnimPlot3D(fig, ax, lines, points, x_solve, plot_speed=11,
                rotation_speed=0.05)
plt.show()
