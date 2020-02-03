from matplotlib.animation import FuncAnimation, PillowWriter
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
    **kwargs   : other arguments passable into
                 matplotlib.animation.FuncAnimation()
    """
    def __init__(self, fig, lines, x, y, trail=True, plot_speed=10,
                 save_as=None, **kwargs):

        def _init():
            lines.set_data([], [])
            return lines,

        if len(x) != len(y):
            raise ValueError('x and y must be the same size.')

        def _animate(i):
            lines.set_data(x[:plot_speed * i], y[:plot_speed * i])
            return lines,

        def _animate_single_point(i):
            lines.set_data(x[plot_speed * i], y[plot_speed * i])
            return lines,

        if trail == True:
            anim = FuncAnimation(fig, _animate, init_func=_init,
                                 interval=1, blit=True, **kwargs)
        else:
            anim = FuncAnimation(fig, _animate_single_point,
                                 init_func=_init, blit=True, **kwargs)

        if save_as is not None:
            anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            pass


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
    l_num          : number of points plotted to 'lines' each frame
    p_num          : number of points plotted to 'points' each frame
    **kwargs       : other arguments passable into
                     matplotlib.animation.FuncAnimation()
    """
    def __init__(self, fig, ax, lines, points, x, y, z, plot_speed=10, 
                 rotation_speed=0, l_num=0, p_num=1, save_as=None,
                 blit=True, **kwargs):

        def _init():
            for self.line, self.point in zip(lines, points):
                self.line.set_data([], [])
                self.line.set_3d_properties([])

                self.point.set_data([], [])
                self.point.set_3d_properties([])
            return lines + points

        def shape_data(x, y, z):
            data = np.array([x, y, z])
            data_transpose = np.array([data]).T
            data_plot = np.reshape(data_transpose, (1, len(x), 3), order='C')
            return data_plot

        def _animate(i):
            array = shape_data(x, y, z)
            i = (plot_speed * i) % array.shape[1]

            for self.line, self.point, self.data in zip(lines, points, array):
                self.x, self.y, self.z = self.data[:i].T
                self.line.set_data(self.x[-l_num:], self.y[-l_num:])
                self.line.set_3d_properties(self.z[-l_num:])

                self.point.set_data(self.x[-p_num:], self.y[-p_num:])
                self.point.set_3d_properties(self.z[-p_num:])

            if rotation_speed != 0:
                ax.view_init(30, rotation_speed * i)
                fig.canvas.draw()
            else:
                pass

            return lines + points

        anim = FuncAnimation(fig, _animate, init_func=_init, interval=1,
                             blit=blit, **kwargs)

        if save_as is not None:
            anim.save(save_as + '.gif', writer=PillowWriter(fps=60))
        else:
            pass
