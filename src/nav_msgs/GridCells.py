# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Point

from typing import Any


class GridCells:
    """
    https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/GridCells.msg

    Args:
        header: No information
        cell_width: No information
        cell_height: No information
        cells: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        cell_width: float32 | float = None,
        cell_height: float32 | float = None,
        cells: list[Point] | list[int] = None,
    ):
        self.header: Header | Any
        self.cell_width: float32 | float
        self.cell_height: float32 | float
        self.cells: list[Point] | list[int]

