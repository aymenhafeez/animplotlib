from matplotlib.animation import FuncAnimation

# TODO: Merge AnimSimple and AnimPlot classes


class AnimSimple:
    """
    Produces an animated 2-D plot. Plots each point rather than all points
    up until the ith point.
    """

    def __init__(self, fig, lines, x, y, **kwargs):

        def _init():
            lines.set_data([], [])
            return lines,

        def _animate(i):
            lines.set_data(x[i], y[i])
            return lines,

        self.anim = FuncAnimation(fig, _animate, init_func=_init, blit=True,
                                  **kwargs)


class AnimPlot:
    '''Produces an animated 2-D plot.'''

    def __init__(self, fig, lines, x, y, plot_speed=10, **kwargs):

        def _init():
            lines.set_data([], [])
            return lines,

        def _animate(i):
            lines.set_data(x[:plot_speed * i], y[:plot_speed * i])
            return lines,

        self.anim = FuncAnimation(fig, _animate, init_func=_init, interval=1, blit=True,
                                  **kwargs)


class AnimPlot3D:

    # TODO: Add array reshape functionality to class
    
    """
    Produces an animated 3-D plot. Array shape must be (1, n, 3), where
    n is the number of data points.

    Parameters:
    ===========
    fig = matplotlib.pyplot.figure()
    ax = axes
    lines = [ax.plot([], [], [])]
    points = [ax.plot([], [], [], 'o')]
    array = (1, n, 3) array
    plot_speed = Natural number 
    rotation_speed = Natural number, proportional to plot_speed
        ---> keep blit=False for this
    l_num = Number of points plotted to lines each frame
    p_num = Number of points plotted to points each frame
    **kwargs = Other arguments passable into matplotlib.animation.FuncAnimation()

    See examples to better understand how to use each parameter.
    """

    def __init__(self, fig, ax, lines, points, array, plot_speed=10,
                 rotation_speed=0.0, l_num=0, p_num=-1, **kwargs):

        def _init():
            for self.line, self.point in zip(lines, points):
                self.line.set_data([], [])
                self.line.set_3d_properties([])

                self.point.set_data([], [])
                self.point.set_3d_properties([])
            return lines + points

        def _animate(i):
            i = (plot_speed * i) % array.shape[1]

            for self.line, self.point, self.data in zip(lines, points, array):
                self.x, self.y, self.z = self.data[:i].T
                self.line.set_data(self.x[-l_num:], self.y[-l_num:])
                self.line.set_3d_properties(self.z[-l_num:])

                self.point.set_data(self.x[-p_num:], self.y[-p_num:])
                self.point.set_3d_properties(self.z[-p_num:])

            ax.view_init(30, rotation_speed * i)
            fig.canvas.draw()

            return lines + points

        self.anim = FuncAnimation(fig, _animate, init_func=_init, interval=1,
                                  **kwargs)
