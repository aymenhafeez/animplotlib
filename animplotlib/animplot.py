import math
from collections.abc import Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
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
        Number of trailing points for the line. Defaults to 0 i.e. the whole line
    p_num : int, optional
        Number of points for the moving point. Defaults to 1 i.e. the current most
        point
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
        l_num: int = 0,
        p_num: int = 1,
        **kwargs,
    ) -> None:
        self.lines = [line] if isinstance(line, Line2D) else list(line)
        self.points = [point] if isinstance(point, Line2D) else list(point)
        self.xs = _series(x)
        self.ys = _series(y)
        self.plot_speed = plot_speed
        self.l_num = l_num
        self.p_num = p_num

        kwargs.setdefault("interval", 1)
        kwargs.setdefault("blit", True)

        if any(len(s) != len(self.lines) for s in (self.points, self.xs, self.ys)):
            raise ValueError(
                "lines, points and x/y data must all have the same number of entries"
            )

        self.anim = FuncAnimation(
            fig,
            self._animate,
            init_func=self._init,
            frames=math.ceil(max(len(x) for x in self.xs) / self.plot_speed),
            **kwargs,
        )

    def save(
        self, path: str, fps: int = 50, dpi: float | None = None, **kwargs
    ) -> None:
        if path.endswith(".gif"):
            kwargs.setdefault("writer", "pillow")

        self.anim.save(path, fps=fps, dpi=dpi, **kwargs)

    def show(self) -> None:
        plt.show()

    def _init(self):
        for line, point in zip(self.lines, self.points):
            line.set_data([], [])
            point.set_data([], [])

        return self.lines + self.points

    def _animate(self, i):
        for x, y, line, point in zip(self.xs, self.ys, self.lines, self.points):
            end = min(self.plot_speed * (i + 1), len(x))
            x_vals, y_vals = x[:end], y[:end]
            line.set_data(x_vals[-self.l_num :], y_vals[-self.l_num :])
            point.set_data(x_vals[-self.p_num :], y_vals[-self.p_num :])

        return self.lines + self.points
