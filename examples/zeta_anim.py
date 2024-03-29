import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
import animplotlib as anim

plt.style.use('dark_background')


x, y = [], []
n_upper = 49

for k in np.arange(0, n_upper, 0.01):
    compl = zeta(complex(0.5, k))
    x.append(compl.real)
    y.append(compl.imag)

fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot([], [], lw=0.5)

ax.set_xlim(-2, 5)
ax.set_ylim(-3, 3)
ax.set_axis_off()

my_animator = anim.AnimPlot(fig, line, x, y, plot_speed = 20)

my_animator.do_animation(save_as = None)
plt.show()
