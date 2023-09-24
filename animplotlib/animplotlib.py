from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np


class AnimPlot:
    """
    Produces an animated 2-D plot.

    Parameters
    ==========
    fig        : matplotlib figure
    lines      : empty matplotlib plot
    x, y       : list; points being plotted
    trail      : if True, all points up to the ith point are plotted each frame
                 if False, only the ith point is plotted each frame
    plot_speed : int
    save_as    : str; file name to save animation as gif to current working
                 directory
    **kwargs   : other arguments passable into
                 matplotlib.animation.FuncAnimation()
    """
    def __init__(self, fig, lines, x, y, plot_speed=10, save_as=None):
        self.x = x
        self.y = y
        self.plot_speed = plot_speed
        self.lines = lines

        def _init():
            self.lines.set_data([], [])
            return self.lines,

        def _animate(i):
            start_idx = 0
            end_idx = min(self.plot_speed * (i + 1), len(self.x))
            self.lines.set_data(self.x[:end_idx], self.y[:end_idx])
            return self.lines,

        anim = FuncAnimation(fig, _animate, init_func=_init, frames=len(x)//plot_speed,
                             interval=1, blit=True)

        if save_as is not None:
            anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            plt.show()


class AnimPlot3D:
    """
    Produces an animated 3-D plot.

    Parameters
    ==========
    fig            : matplotlib figure
    ax             : matplotlib axes
    lines          : empty matplotlib plot contained in a list
    points         : empty matplotlib plot contained in a list; shows the
                     ith point being plotted
    x, y, z        : list; points being plotted
    plot_speed     : int
    rotation_speed : int; proportional to plot_speed
                     ---> keep blit=False (default) for this
    l_num          : int; number of points plotted to 'lines' each frame
    p_num          : int; number of points plotted to 'points' each frame
    save_as        : str; file name to save animation as gif to current working
                     directory
    **kwargs       : other arguments passable into
                     matplotlib.animation.FuncAnimation()
    """
    def __init__(self, fig, ax, lines, points, x, y, z, plot_speed=10,
                 rotation_speed=0, l_num=0, p_num=1, save_as=None,
                 blit=True, **kwargs):

        self.fig = fig
        self.ax = ax
        self.lines = lines
        self.points = points
        self.x = x
        self.y = y
        self.z = z
        self.plot_speed = plot_speed
        self.rotation_speed = rotation_speed
        self.l_num = l_num
        self.p_num = p_num

        def _init():
            empty_array = np.array([], dtype=float)
            for line, point in zip(self.lines, self.points):
                line.set_data(empty_array, empty_array)
                line.set_3d_properties(empty_array)

                point.set_data(empty_array, empty_array)
                point.set_3d_properties(empty_array)
            return self.lines + self.points

        def _animate(i):
            i = (self.plot_speed * i) % len(self.x)

            for line, point in zip(self.lines, self.points):
                x_vals, y_vals, z_vals = self.x[:i], self.y[:i], self.z[:i]
                line.set_data(x_vals[-self.l_num:], y_vals[-self.l_num:])
                line.set_3d_properties(z_vals[-self.l_num:])

                point.set_data(x_vals[-self.p_num:], y_vals[-self.p_num:])
                point.set_3d_properties(z_vals[-self.p_num:])

            if self.rotation_speed != 0:
                self.ax.view_init(30, self.rotation_speed * i)
                self.fig.canvas.draw()

            return self.lines + self.points

        self.anim = FuncAnimation(self.fig, _animate, init_func=_init, interval=1,
                                 blit=blit, **kwargs)

        if save_as is not None:
            self.anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
