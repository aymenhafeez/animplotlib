import animplotlib as anim
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

x0 = [0, 1, 15]
t = np.linspace(0.01, 50, 10000)


def lorenz(x_var, t, sigma, rho, beta):
    x, y, z = x_var
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]


def solve_lorenz(x0, t, sigma, rho, beta):
    return odeint(lorenz, x0, t, args=(sigma, rho, beta))


x_solve = solve_lorenz(x0, t, sigma=10, rho=28, beta=8 / 3)
x, y, z = x_solve.T

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

lines = ax.plot([], [], [])
points = ax.plot([], [], [], "ro", lw=1, markersize=8)
ax.set_title("Lorenz Attractor")
ax.set_axis_off()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))

anim.AnimPlot3D(fig, ax, lines, points, x, y, z, plot_speed=3, rotation_speed=0.1)
