from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
import math

class AnimPlot:
    """
    Produces an animated 2-D plot.
    """
    def __init__(self, fig, line, point, x, y, plot_speed=10, l_num=1,
                 p_num=1, save_as=None, **kwargs):
        self.x = np.asarray(x)
        self.y = np.asarray(y)
        self.plot_speed = plot_speed
        self.line = line
        self.point = point
        self.l_num = l_num
        self.p_num = p_num
        self.save_as = save_as
        self.kwargs = kwargs

        self.anim = FuncAnimation(
            fig, self._animate, init_func=self._init,
            frames=math.ceil(len(self.x) / self.plot_speed),
            interval=1, blit=True, **kwargs
        )

        if save_as is not None:
            self.anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            plt.show()

    def _init(self):
        self.line.set_data([], [])
        self.point.set_data([], [])
        return self.line, self.point

    def _animate(self, i):
        end_idx = min(self.plot_speed * (i + 1), len(self.x))
        trailing_x = self.x[max(0, end_idx - self.l_num):end_idx]
        trailing_y = self.y[max(0, end_idx - self.l_num):end_idx]
        current_x = self.x[end_idx - self.p_num:end_idx]
        current_y = self.y[end_idx - self.p_num:end_idx]
        self.line.set_data(trailing_x, trailing_y)
        self.point.set_data(current_x, current_y)
        return self.line, self.point


class AnimPlot3D:
    """
    Produces an animated 3-D plot.
    """
    def __init__(self, fig, ax, lines, points, x, y, z, plot_speed=10,
                 rotation_speed=0, l_num=0, p_num=1, save_as=None,
                 blit=True, **kwargs):
        self.fig = fig
        self.ax = ax
        self.lines = lines
        self.points = points
        self.x = np.asarray(x)
        self.y = np.asarray(y)
        self.z = np.asarray(z)
        self.plot_speed = plot_speed
        self.rotation_speed = rotation_speed
        self.l_num = l_num
        self.p_num = p_num
        self.save_as = save_as
        self.kwargs = kwargs

        self.anim = FuncAnimation(
            self.fig, self._animate, init_func=self._init,
            frames=len(self.x) // self.plot_speed,
            interval=1, blit=blit, **kwargs
        )

        if save_as is not None:
            self.anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            plt.show()

    def _init(self):
        for line, point in zip(self.lines, self.points):
            line.set_data([], [])
            line.set_3d_properties([])
            point.set_data([], [])
            point.set_3d_properties([])
        return self.lines + self.points

    def _animate(self, i):
        idx = (self.plot_speed * i) % len(self.x)
        for line, point in zip(self.lines, self.points):
            x_vals, y_vals, z_vals = self.x[:idx], self.y[:idx], self.z[:idx]
            line.set_data(x_vals[-self.l_num:], y_vals[-self.l_num:])
            line.set_3d_properties(z_vals[-self.l_num:])
            point.set_data(x_vals[-self.p_num:], y_vals[-self.p_num:])
            point.set_3d_properties(z_vals[-self.p_num:])
        if self.rotation_speed != 0:
            self.ax.view_init(30, self.rotation_speed * idx)
            self.fig.canvas.draw()
        return self.lines + self.points
