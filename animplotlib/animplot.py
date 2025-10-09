from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
import math


class AnimPlot:
    """
    Produces animated 2-D plots for one or more projections.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to animate.
    line : Line2D or list of Line2D
        The line(s) to update.
    point : Line2D or list of Line2D
        The point(s) to update.
    x : array-like or list of array-like
        X data for each plot.
    y : array-like or list of array-like
        Y data for each plot.
    plot_speed : int, optional
        Number of points to add per frame.
    l_num : int, optional
        Number of trailing points for the line.
    p_num : int, optional
        Number of points for the moving point.
    save_as : str or None, optional
        If set, saves animation as GIF with this name.
    **kwargs : dict
        Additional arguments for FuncAnimation.
    """
    def __init__(self, fig, line, point, x, y, plot_speed=10, l_num=10,
                 p_num=1, save_as=None, **kwargs):
        self.lines = line if isinstance(line, (list, tuple)) else [line]
        self.points = point if isinstance(point, (list, tuple)) else [point]
        self.xs = [np.asarray(arr) for arr in (x if isinstance(x, (list, tuple)) else [x])]
        self.ys = [np.asarray(arr) for arr in (y if isinstance(y, (list, tuple)) else [y])]
        self.plot_speed = plot_speed
        self.l_num = l_num
        self.p_num = p_num
        self.save_as = save_as
        self.kwargs = kwargs

        self.anim = FuncAnimation(
            fig, self._animate, init_func=self._init,
            frames=math.ceil(len(self.xs[0]) / self.plot_speed),
            interval=1, blit=True, **kwargs
        )

        if save_as is not None:
            self.anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            plt.show()

    def _init(self):
        for line, point in zip(self.lines, self.points):
            line.set_data([], [])
            point.set_data([], [])
        return self.lines + self.points

    def _animate(self, i):
        end_idx = min(self.plot_speed * (i + 1), len(self.xs[0]))
        artists = []
        for x, y, line, point in zip(self.xs, self.ys, self.lines, self.points):
            trailing_x = x[max(0, end_idx - self.l_num):end_idx]
            trailing_y = y[max(0, end_idx - self.l_num):end_idx]
            current_x = x[end_idx - self.p_num:end_idx]
            current_y = y[end_idx - self.p_num:end_idx]
            line.set_data(trailing_x, trailing_y)
            point.set_data(current_x, current_y)
            artists.extend([line, point])
        return artists
