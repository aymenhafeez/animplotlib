import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import animplotlib as anim

sigma = 10
rho = 28
beta = 8/3
x0 = [0, 1, 15]
t = np.linspace(0.01, 100, 10000)

def lorenz(x_var, t):
    x = x_var[0]
    y = x_var[1]
    z = x_var[2]
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

x_solve = odeint(lorenz, x0, t)
x = x_solve[:, 0]
y = x_solve[:, 1]
z = x_solve[:, 2]

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=0.5)
point, = ax.plot([], [], 'ro', markersize=4)

ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))

anim.AnimPlot(fig, line, point, x, y, plot_speed=10, l_num=len(t))
