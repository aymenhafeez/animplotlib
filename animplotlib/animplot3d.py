import math
from collections.abc import Sequence

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
from numpy.typing import ArrayLike

from .animplot import _series


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
        Rotation speed(s) for each subplot (degrees per data point).
    l_num : int, optional
        Number of trailing points for the line.
    p_num : int, optional
        Number of points for the moving point.
    blit : bool, optional
        Should be False for 3D plots.
    **kwargs : dict
        Additional arguments for FuncAnimation.
    """

    def __init__(
        self,
        fig: Figure,
        ax: Axes3D | Sequence[Axes3D],
        lines: Line3D | Sequence[Line3D],
        points: Line3D | Sequence[Line3D],
        x: ArrayLike | Sequence[ArrayLike],
        y: ArrayLike | Sequence[ArrayLike],
        z: ArrayLike | Sequence[ArrayLike],
        plot_speed: int = 10,
        rotation_speed: float | Sequence[float] = 0,
        l_num: int = 0,
        p_num: int = 1,
        blit: bool = False,
        **kwargs,
    ) -> None:
        self.fig = fig
        self.lines = [lines] if isinstance(lines, Line3D) else list(lines)
        self.points = [points] if isinstance(points, Line3D) else list(points)
        self.axes = [ax] * len(self.lines) if isinstance(ax, Axes3D) else list(ax)
        self.xs = _series(x)
        self.ys = _series(y)
        self.zs = _series(z)
        self.plot_speed = plot_speed
        self.rotation_speeds = (
            [rotation_speed] * len(self.axes)
            if isinstance(rotation_speed, (int, float))
            else list(rotation_speed)
        )
        self.l_num = l_num
        self.p_num = p_num

        kwargs.setdefault("interval", 1)

        if any(
            len(s) != len(self.lines)
            for s in (
                self.points,
                self.axes,
                self.rotation_speeds,
                self.xs,
                self.ys,
                self.zs,
            )
        ):
            raise ValueError(
                "lines, points, axes, rotation speeds and x/y/z data must all have the same number of entries"
            )

        self.anim = FuncAnimation(
            self.fig,
            self._animate,
            init_func=self._init,
            frames=math.ceil(len(self.xs[0]) / self.plot_speed),
            blit=blit,
            **kwargs,
        )

    def save(
        self, path: str, fps: int = 50, dpi: float | None = None, **kwargs
    ) -> None:
        if path.endswith(".gif"):
            kwargs.setdefault("writer", "pillow")

        # default dpi in matplotlib = 100
        # if no dpi gets set matplotlib uses the figures default dpi (figsize * 100)
        self.anim.save(path, fps=fps, dpi=dpi, **kwargs)

    def show(self) -> None:
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
            self.xs,
            self.ys,
            self.zs,
            self.lines,
            self.points,
            self.axes,
            self.rotation_speeds,
        ):
            x_vals, y_vals, z_vals = x[:end_idx], y[:end_idx], z[:end_idx]
            line.set_data(x_vals[-self.l_num :], y_vals[-self.l_num :])
            line.set_3d_properties(z_vals[-self.l_num :])
            point.set_data(x_vals[-self.p_num :], y_vals[-self.p_num :])
            point.set_3d_properties(z_vals[-self.p_num :])
            if rot_speed != 0:
                ax.view_init(30, rot_speed * end_idx)
        return self.lines + self.points
