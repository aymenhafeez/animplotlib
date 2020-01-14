import animplotlib as anim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint

plt.style.use('dark_background')

sigma = 10
rho = 50
beta = 8/3
x0 = [0, 1, 20]
t_s, t_m = 0, 75
t = np.linspace(t_s, t_m, 15000)


def lorenz(x_var, t):
    x = x_var[0]
    y = x_var[1]
    z = x_var[2]

    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z

    return [dx_dt, dy_dt, dz_dt]


x_solve = np.array([odeint(lorenz, x0, t)])

x = x_solve[0, :, 0]
y = x_solve[0, :, 1]
z = x_solve[0, :, 2]

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

lines, = [ax.plot([], [], [], lw=0.25)]
points, = [ax.plot([], [], [], 'o', markerfacecolor='None', markersize=4.5,
                   markeredgewidth=0.25)]

ax.set_xlim((-25, 25))
ax.set_ylim((-45, 45))
ax.set_zlim((15, 85))
ax.set_axis_off()

anim.AnimPlot3D(fig, ax, lines, points, x, y, z, plot_speed=7,
                rotation_speed=0.1, p_num=1)

plt.show()
