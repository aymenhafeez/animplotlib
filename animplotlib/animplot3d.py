from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
import math


class AnimPlot3D:
    """
    Produces animated 3-D plots for one or more projections.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to animate.
    ax : Axes3D or list of Axes3D
        The axes to update.
    lines : Line3D or list of Line3D
        The line(s) to update.
    points : Line3D or list of Line3D
        The point(s) to update.
    x, y, z : array-like or list of array-like
        Data for each plot.
    plot_speed : int, optional
        Number of points to add per frame.
    rotation_speed : float or list of float, optional
        Rotation speed(s) for each subplot (degrees per frame).
    l_num : int, optional
        Number of trailing points for the line.
    p_num : int, optional
        Number of points for the moving point.
    save_as : str or None, optional
        If set, saves animation as GIF with this name.
    blit : bool, optional
        Should be False for 3D plots.
    **kwargs : dict
        Additional arguments for FuncAnimation.
    """
    def __init__(self, fig, ax, lines, points, x, y, z, plot_speed=10,
                 rotation_speed=0, l_num=0, p_num=1, save_as=None,
                 blit=False, **kwargs):
        self.fig = fig
        self.axes = ax if isinstance(ax, (list, tuple)) else [ax]
        self.lines = lines if isinstance(lines, (list, tuple)) else [lines]
        self.points = points if isinstance(points, (list, tuple)) else [points]
        self.xs = [np.asarray(arr) for arr in (x if isinstance(x, (list, tuple)) else [x])]
        self.ys = [np.asarray(arr) for arr in (y if isinstance(y, (list, tuple)) else [y])]
        self.zs = [np.asarray(arr) for arr in (z if isinstance(z, (list, tuple)) else [z])]
        self.plot_speed = plot_speed
        self.rotation_speeds = (rotation_speed if isinstance(rotation_speed, (list, tuple))
                                else [rotation_speed] * len(self.axes))
        self.l_num = l_num
        self.p_num = p_num
        self.save_as = save_as
        self.kwargs = kwargs

        self.anim = FuncAnimation(
            self.fig, self._animate, init_func=self._init,
            frames=math.ceil(len(self.xs[0]) / self.plot_speed),
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
        end_idx = min(self.plot_speed * (i + 1), len(self.xs[0]))
        for x, y, z, line, point, ax, rot_speed in zip(
                self.xs, self.ys, self.zs, self.lines, self.points, self.axes, self.rotation_speeds):
            x_vals, y_vals, z_vals = x[:end_idx], y[:end_idx], z[:end_idx]
            line.set_data(x_vals[-self.l_num:], y_vals[-self.l_num:])
            line.set_3d_properties(z_vals[-self.l_num:])
            point.set_data(x_vals[-self.p_num:], y_vals[-self.p_num:])
            point.set_3d_properties(z_vals[-self.p_num:])
            if rot_speed != 0:
                ax.view_init(30, rot_speed * end_idx)
        return self.lines + self.points
