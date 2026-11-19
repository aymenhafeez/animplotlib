import math
from collections.abc import Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from numpy.typing import ArrayLike


def _series(data):
    if np.ndim(data[0]) == 0:
        data = [data]

    return [np.asarray(arr) for arr in data]


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

    def __init__(
        self,
        fig: Figure,
        line: Line2D | Sequence[Line2D],
        point: Line2D | Sequence[Line2D],
        x: ArrayLike | Sequence[ArrayLike],
        y: ArrayLike | Sequence[ArrayLike],
        plot_speed: int = 10,
        l_num: int = 10,
        p_num: int = 1,
        save_as: str | None = None,
        **kwargs,
    ) -> None:
        self.lines = [line] if isinstance(line, Line2D) else list(line)
        self.points = [point] if isinstance(point, Line2D) else list(point)
        self.xs = _series(x)
        self.ys = _series(y)
        self.plot_speed = plot_speed
        self.l_num = l_num
        self.p_num = p_num
        self.save_as = save_as
        self.kwargs = kwargs

        kwargs.setdefault("interval", 1)
        kwargs.setdefault("blit", True)

        if any(len(s) != len(self.lines) for s in (self.points, self.xs, self.ys)):
            raise ValueError(
                "lines, points, axes, and x/y data must all have the same number of entries"
            )

        self.anim = FuncAnimation(
            fig,
            self._animate,
            init_func=self._init,
            frames=math.ceil(len(self.xs[0]) / self.plot_speed),
            **kwargs,
        )

        if save_as is not None:
            self.anim.save(save_as + ".gif", writer=PillowWriter(fps=60))
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
            trailing_x = x[max(0, end_idx - self.l_num) : end_idx]
            trailing_y = y[max(0, end_idx - self.l_num) : end_idx]
            current_x = x[end_idx - self.p_num : end_idx]
            current_y = y[end_idx - self.p_num : end_idx]
            line.set_data(trailing_x, trailing_y)
            point.set_data(current_x, current_y)
            artists.extend([line, point])
        return artists
