import animplotlib as anim
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

t = np.linspace(0.01, 75, 15000)
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

epsilon = 1e-2
x0 = [(1.1, 2.1, -2 + n * epsilon) for n in range(len(colours))]


def dadras(x_var, t, a, b, c, d, e):
    x, y, z = x_var
    dxdt = y - a * x + b * y * z
    dydt = c * y - x * z + z
    dzdt = d * x * y - e * z
    return [dxdt, dydt, dzdt]


def solve_dadras(x0, t, a, b, c, d, e):
    return odeint(dadras, x0, t, args=(a, b, c, d, e))


plt.style.use(("dark_background"))
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

lines = []
points = []
xs, ys, zs = [], [], []

for init_cond, colour in zip(x0, colours):
    x_solve = solve_dadras(init_cond, t, a=3, b=2.7, c=1.7, d=2, e=9)
    x, y, z = x_solve.T
    xs.append(x)
    ys.append(y)
    zs.append(z)
    (line,) = ax.plot([], [], [], lw=2, c=colour)
    (point,) = ax.plot([], [], [], "o", c=colour, markersize=0)
    lines.append(line)
    points.append(point)

ax.set_xlim(np.min(xs), np.max(xs))
ax.set_ylim(np.min(ys), np.max(ys))
ax.set_zlim(np.min(zs), np.max(zs))
ax.set_axis_off()
plt.tight_layout()

anim.AnimPlot3D(
    fig,
    [ax] * len(lines),
    lines,
    points,
    xs,
    ys,
    zs,
    plot_speed=13,
    rotation_speed=0.05,
    l_num=350,
    p_num=1,
    # save_as="dadras_multi",
)
