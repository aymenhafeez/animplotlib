from typing import Any, List, Union

import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

class AnimPlot:
    lines: List[Line2D]
    points: List[Line2D]
    xs: List[np.ndarray]
    ys: List[np.ndarray]
    plot_speed: int
    l_num: int
    p_num: int
    save_as: Union[str, None]
    kwargs: Any
    anim: FuncAnimation
    def __init__(
        self,
        fig: Figure,
        line: Union[Line2D, List[Line2D]],
        point: Union[Line2D, List[Line2D]],
        x: Union[np.ndarray, List[np.ndarray]],
        y: Union[np.ndarray, List[np.ndarray]],
        plot_speed: int = 10,
        l_num: int = 10,
        p_num: int = 1,
        save_as: Union[str, None] = None,
        **kwargs: Any,
    ) -> None: ...
    def _init(self) -> List[Line2D]: ...
    def _animate(self, i: int) -> List[Line2D]: ...
