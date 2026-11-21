# animplotlib API Documentation

## AnimPlot

Class for producing 2D animated plots for one or more projections.

Constructor:

```python
AnimPlot(fig, line, point, x, y, plot_speed=10, l_num=0, p_num=1, **kwargs)
```

**Parameters:**

* `fig`: `matplotlib.figure.Figure`\
  The figure to animate.
* `line`: `Line2D` or list of `Line2D`\
  The line(s) to update.
* `point`: `Line2D` or list of `Line2D`\
  The point(s) to update.
* `x`, `y`: array-like or list of array-like\
  Data for each plot.
* `plot_speed`: `int`, optional\
  Number of points to add per frame.
* `l_num`: `int`, optional\
  Number of trailing points for the line. Defaults to 0 so all points up to the current
  most point are shown each frame.
* `p_num`: `int`, optional\
  Number of points for the moving point. Defaults to 1 so just the current most point is
  shown each frame.
* `**kwargs`: Additional arguments for `FuncAnimation`.

**Example:**

```python
from animplotlib import AnimPlot
a = AnimPlot(fig, line, point, x, y, plot_speed=2, l_num=50)
a.show()  # a.save("animation.gif")
```

## AnimPlot3D

Class for producing 3D animated plots for one or more projections.

Constructor:

```python
AnimPlot3D(
    fig, ax, lines, points, x, y, z, plot_speed=10, rotation_speed=0, l_num=0, p_num=1, blit=False, **kwargs
)
```

**Parameters:**

* `fig`: `matplotlib.figure.Figure`\
  The figure to animate.
* `ax`: `Axes3D` or list of `Axes3D`\
  The axes to update.
* `lines`: `Line3D` or list of `Line3D`\
  The line(s) to update.
* `points`: `Line3D` or list of `Line3D`\
  The point(s) to update.
* `x`, `y`, `z`: array-like or list of array-like\
  Data for each plot.
* `plot_speed`: `int`, optional\
  Number of points to add per frame.
* `rotation_speed`: `float` or list of `float`, optional\
  Rotation speed(s) for each subplot (degrees per data point).
* `l_num`: `int`, optional\
  Number of trailing points for the line.
* `p_num`: `int`, optional\
  Number of points for the moving point.
* `blit`: `bool`, optional\
  If True, only redraw the parts of the figure that change on update. Defaults to False
* `**kwargs`: Additional arguments for `FuncAnimation`.

**Example:**

```python
from animplotlib import AnimPlot3D
a = AnimPlot3D(fig, ax, line, point, x, y, z, plot_speed=2, l_num=50)
a.show()  # a.save("animation.gif")
```

## Methods

Both `AnimPlot` and `AnimPlot3D` have the following methods:

```python
a.save(path, fps=50, dpi=None, **kwargs)
```

**Parameters**:

* `path`: `str`\
  path to save the animation to. `.gif` files are written with Pillow, other formats,
  such as MP4 require ffmpeg.
* `fps`: `int`, optional\
  number of frames per second in the saved animation. Defaults to 50.
* `dpi`: `float`, optional\
  resolution of the saved file. Defaults to the figure's dpi (100) so the output is
  `figsize * dpi` pixels.
* `**kwargs`: Additional arguments for
  [`matplotlib.animation.Animation.save()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save).

```python
a.show()
```

* Wraps [`matplotlib.pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html). Display every open figure.

## Save quality

The following can be used to control the quality of the saved animation:

* **Resolution**: increasing `dpi` will give sharper output e.g. `a.save("out.mp4",
  dpi=300)`. Things like line width and text scale with it.
* **MP4 compression**: an `extra_args` argument can be passed which is a list of command
  line flags that get passed to ffmpeg. The most useful is probably the constant rate
  factor which controls the MP4 quality. A lower value is better, with 18 being close to
  lossless and 23 being ffmpeg's default, e.g. `a.save("out.mp4", extra_args=["-crf",
  "18"])`. See ffmpeg's [H.264 encoding
  guide](https://trac.ffmpeg.org/wiki/Encode/H.264) for other options. Note that
  `extra_args` only works with the ffmpeg writer, which is the default for MP4. For gifs
  explicitly pass `writer="ffmpeg"`.
* **GIFs**: limited to 256 colours per frame and grow quickly with `dpi`. MP4s will give
  a much smaller file size for the same resolution.

## Advanced Usage

[See here](https://aymenhafeez.github.io/posts/2025-10-09-animplotlib/) for some more advanced examples,
such as animating multiple plots on the same figure, animating multiple plots on
separate axes, and more.

## License

MIT
