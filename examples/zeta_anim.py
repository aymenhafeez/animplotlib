from animplotlib import AnimPlot
import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta

x, y = [], []
n_upper = 49

for k in np.arange(0, n_upper, 0.01):
    compl = zeta(complex(0.5, k))
    x.append(compl.real)
    y.append(compl.imag)

fig = plt.figure()
ax = fig.add_subplot(111)

line = ax.plot([], [], lw=1)
point = ax.plot([], [], "o", markersize=5)

ax.set_xlim(-2, 5)
ax.set_ylim(-3, 3)

a = AnimPlot(fig, line, point, x, y, plot_speed=1)
a.show()
