from typing import Any, List, Union

import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure

class AnimPlot3D:
    fig: Figure
    axes: List[Any]
    lines: List[Any]
    points: List[Any]
    xs: List[np.ndarray]
    ys: List[np.ndarray]
    zs: List[np.ndarray]
    plot_speed: int
    rotation_speeds: List[float]
    l_num: int
    p_num: int
    save_as: Union[str, None]
    kwargs: Any
    anim: FuncAnimation
    def __init__(
        self,
        fig: Figure,
        ax: Union[Any, List[Any]],
        lines: Union[Any, List[Any]],
        points: Union[Any, List[Any]],
        x: Union[np.ndarray, List[np.ndarray]],
        y: Union[np.ndarray, List[np.ndarray]],
        z: Union[np.ndarray, List[np.ndarray]],
        plot_speed: int = 10,
        rotation_speed: Union[float, List[float]] = 0,
        l_num: int = 0,
        p_num: int = 1,
        save_as: Union[str, None] = None,
        blit: bool = False,
        **kwargs: Any,
    ) -> None: ...
    def _init(self) -> List[Any]: ...
    def _animate(self, i: int) -> List[Any]: ...
