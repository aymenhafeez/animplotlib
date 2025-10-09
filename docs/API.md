# animplotlib API Documentation

This document provides an overview of the API for the `animplotlib` library,
which is designed for creating animated plots using Matplotlib.

---

## Animplot

Class for producing 2D animated plots for one or more projections.

Constructor:
```python
AnimPlot(fig, line, point, x, y, plot_speed=10, l_num=10, p_num=1, save_as=None, **kwargs)
```

**Parameters:**
- `fig`: `matplotlib.figure.Figure`  
  The figure to animate.
- `line`: `Line2D` or list of `Line2D`  
  The line(s) to update.
- `point`: `Line2D` or list of `Line2D`  
  The point(s) to update.
- `x`, `y`: array-like or list of array-like  
  Data for each plot.
- `plot_speed`: `int`, optional  
  Number of points to add per frame.
- `l_num`: `int`, optional  
  Number of trailing points for the line.
- `p_num`: `int`, optional  
  Number of points for the moving point.
- `save_as`: `str` or `None`, optional  
  If set, saves animation as GIF with this name.
- `**kwargs`: Additional arguments for `FuncAnimation`.

**Example:**
```python
from animplotlib import AnimPlot
AnimPlot(fig, line, point, x, y, plot_speed=2, l_num=50)
```

---

## Animplot3D

Class for producing 3D animated plots for one or more projections.

Constructor:
```python
AnimPlot3D(fig, ax, lines, points, x, y, z, plot_speed=10, rotation_speed=0, l_num=0, p_num=1, save_as=None, blit=False, **kwargs)
```

**Parameters:**
- `fig`: `matplotlib.figure.Figure`  
  The figure to animate.
- `ax`: `Axes3D` or list of `Axes3D`  
  The axes to update.
- `lines`: `Line3D` or list of `Line3D`  
  The line(s) to update.
- `points`: `Line3D` or list of `Line3D`  
  The point(s) to update.
- `x`, `y`, `z`: array-like or list of array-like  
  Data for each plot.
- `plot_speed`: `int`, optional  
  Number of points to add per frame.
- `rotation_speed`: `float` or list of `float`, optional  
  Rotation speed(s) for each subplot (degrees per frame).
- `l_num`: `int`, optional  
  Number of trailing points for the line.
- `p_num`: `int`, optional  
  Number of points for the moving point.
- `save_as`: `str` or `None`, optional  
  If set, saves animation as GIF with this name.
- `blit`: `bool`, optional  
  Should be `False` for 3D plots.
- `**kwargs`: Additional arguments for `FuncAnimation`.

**Example:**
```python
from animplotlib import AnimPlot3D
AnimPlot3D(fig, ax, line, point, x, y, z, plot_speed=2, l_num=50, blit=False)
```

---

## Advanced Usage

Support for multiple subplots in the same figure was recently added. This can
be done by passing a list for axes, lines, points and the data being plotted.
See [this post]() for some more advanced examples.

---

## License

MIT
