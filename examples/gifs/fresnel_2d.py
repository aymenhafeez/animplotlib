import numpy as np
import matplotlib.pyplot as plt
import testanim as anim
import scipy.special as sc

x = np.linspace(-7, 7, 5000)
y, z = sc.fresnel(x)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'o', markersize=5)

ax.set_xlim(np.min(y), np.max(y))
ax.set_ylim(np.min(z), np.max(z))
ax.set_title("Animated 2D Fresnel Plot")

anim.AnimPlot(fig, line, point, y, z, plot_speed=35, l_num=len(x), save_as='fresnel_2d')
