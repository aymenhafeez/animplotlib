from matplotlib.animation import FuncAnimation


class AnimPlot:
    '''Produces an animated 2-D plot.'''

    def __init__(self, fig, lines, x, y, plot_speed=10, **kwargs):

        def _init():
            lines.set_data([], [])
            return lines,

        def _animate(i):
            lines.set_data(x[:plot_speed * i], y[:plot_speed * i])
            return lines,

        self.anim = FuncAnimation(fig, _animate, init_func=_init, interval=1,
                                  blit=True, **kwargs)


class AnimPlot3D:
    '''Produces an animated 3-D plot. Array shape must be (1, n, 3), where
    n is the number of data points.'''

    def __init__(self, fig, ax, lines, points, array, plot_speed=10,
                 rotation_speed=0.0, **kwargs):

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
                self.line.set_data(self.x, self.y)
                self.line.set_3d_properties(self.z)

                self.point.set_data(self.x[-1:], self.y[-1:])
                self.point.set_3d_properties(self.z[-1:])

            ax.view_init(30, rotation_speed * i)
            fig.canvas.draw()

            return lines + points

        self.anim = FuncAnimation(fig, _animate, init_func=_init, interval=1,
                                  **kwargs)
