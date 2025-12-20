import animplotlib as anim  # type: ignore
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

t = np.linspace(0.01, 75, 12500)
colours = [
    "#4E79A7",
    "#F28E2B",
    "#46ACB8",
    "#E15759",
    "#4E79A7",
    "#F28E2B",
    "#4E79A7",
    "#F28E2B",
    "#46ACB8",
    "#E15759",
    "#4E79A7",
    "#F28E2B",
    "#4E79A7",
    "#4E79A7",
    "#F28E2B",
    "#F28E2B",
]

# x0 = [(10.0, 10.0, 10.0), (15.0, 10.0, 20.0), (-15.0, -10.0, 30.0), (5.0, -20.0, 40.0)]
epsilon = 1e-5
x0 = [(10.0, 10.0, 10.0 + n * epsilon) for n in range(len(colours))]


def lorenz(x_var, t, sigma, rho, beta):
    x, y, z = x_var
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def solve_lorenz(x0, t, sigma, rho, beta):
    return odeint(lorenz, x0, t, args=(sigma, rho, beta))


plt.style.use("dark_background")
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
ax.set_axis_off()

lines = []
points = []
xs, ys, zs = [], [], []

for init_cond, colour in zip(x0, colours):
    x_solve = solve_lorenz(init_cond, t, sigma=10, rho=28, beta=8 / 3)
    x, y, z = x_solve.T
    xs.append(x)
    ys.append(y)
    zs.append(z)
    (line,) = ax.plot([], [], [], lw=2, color=colour)
    (point,) = ax.plot([], [], [], "o", color=colour, markersize=0)
    lines.append(line)
    points.append(point)

ax.set_xlim(np.min(xs), np.max(xs))
ax.set_ylim(np.min(ys), np.max(ys))
ax.set_zlim(np.min(zs), np.max(zs))
plt.tight_layout()

anim.AnimPlot3D(
    fig,
    [ax] * len(lines),
    lines,
    points,
    xs,
    ys,
    zs,
    plot_speed=5,
    rotation_speed=0.1,
    l_num=150,
    p_num=1,
    # save_as="lorenz_colour",
)
