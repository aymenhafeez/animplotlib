# animplotlib

This package acts as a thin wrapper around the
`matplotlib.animation.FuncAnimation` class to simplify animating `matplotlib`
plots.

![](examples/gifs/trefoil-knot.gif)

## Installation

```
pip install animplotlib
```


## User manual

There are two classes which can be called: `AnimPlot`, for 2-D plots,
and `AnimPlot3D`, for 3-D plots.

### AnimPlot

As an example, below is a demonstration of the steps required to make a
basic plot of an Euler spiral. An Euler spiral can be obtained by plotting
the [Fresnel integrals](https://en.wikipedia.org/wiki/Fresnel_integral),
which can be generated using `scipy.special`.

Import the necessary libraries and generate the points being plotted, in this
case the fresnel integrals:

```python
import animplotlib as anim
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

x = np.linspace(-7, 7, 5000)
y, z = sc.fresnel(x)

```

Create a figure and axis and then add two empty `matplotlib` plots: one to plot the points
up to the current most point (i.e. the 'line') and one to plot the current most
point:

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'o')

ax.set_xlim(np.min(y), np.max(y))
ax.set_ylim(np.min(z), np.max(z))
ax.set_title("Animated 2D Fresnel Plot")
```
 
Call the `AnimPlot` class:

```python
anim.AnimPlot(fig, line, point, y, z, plot_speed=5, l_num=len(x))
```

`l_num` is the number of points before the current most point being plotted to
`line`. The default value is set to 10, however in this example it makes sense
to set it to the same length as `x` (i.e. all the points before the current
most point are plotted). Think of this as a trail. Similarly, an argument
`p_num` can be passed to determine the number of points being plotted to
`point`. This is set to 1 by default.

Optional arguments:
* `plot_speed` (`int`) : set to 10 by default.
* `l_num` (`int`) : The number of points being plotted to `line` each frame. By
default this is set to 10.
* `p_num` (`int`) : The number of points being plotted to `point` each frame. By
default, this is set to 1, i.e. only the current most point is plotted each
frame (the orange point in the gif).
* `save_as` (`str`) : file name to save the animation as a gif in the
  current working directory.
* `**kwargs` : other arguments passable into
`matplotlib.animation.FuncAnimation` (see [the docs](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.animation.FuncAnimation.html) for more info).

<!-- ![](examples/gifs/fresnel_2d.gif =450x331) -->

<center>
  <figure> 
    <img src="https://raw.githubusercontent.com/aymenhafeez/animplotlib/master/examples/gifs/fresnel_2.gif" height='331' width='450' /> 
  </figure>
</center>

### AnimPlot3D

Creating a 3-D animated plot is very similar to creating a 2-D animated plot.
Continuing with the Euler spiral example, the first step again is to import the
necessary libraries and generate the points being plotted:

```python
import animplotlib as anim
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

x = np.linspace(-7, 7, 5000)
y, z = sc.fresnel(x)
```

Next, create a figure and axis with 3-D projection and then add two empty
plots, this time with three list inputs:

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lines, = ax.plot([], [], [], lw=1)
points, = ax.plot([], [], [], 'ro', markersize=5)
```

After that set the x, y and z limits and call the `AnimPlot3D` class.

```python
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))
ax.set_title("Animated 3D Fresnel Plot")

anim.AnimPlot3D(fig, ax, [lines], [points], x, y, z, plot_speed=5)
```

<!-- ![](examples/gifs/fresnel_3d.gif =450x402) -->

<center>
  <figure> 
    <img src="https://raw.githubusercontent.com/aymenhafeez/animplotlib/master/examples/gifs/fresnel_3d.gif" height='402' width='450' /> 
  </figure>
</center>

Optional arguments:
* `plot_speed` (`int`) : set to 10 by default.
* `rotation_speed` (`int`) : Off by default, enabled by setting a value.
* `l_num` (`int`) : The number of points being plotted to `lines` each frame. By
default, all the points up until the current point get plotted (`l_num=0`.
* `p_num` (`int`) : The number of points being plotted to `points` each frame. By
default, this is set to 1, i.e. only the current most point is plotted each
frame (the red point in the gif).
* `save_as` (`str`) : file name to save the animation as a gif in the
  current working directory.
* `**kwargs` : other arguments passable into
`matplotlib.animation.FuncAnimation` (see [the
docs](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.animation.FuncAnimation.html)
for more info).

Both the 2-D and 3-D plots can be customised visually the same way you would
a normal `matplotlib` plot.
