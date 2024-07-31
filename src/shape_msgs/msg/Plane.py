# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Plane:
    """
    https://github.com/ros2/common_interfaces/blob/humble/shape_msgs/msg/Plane.msg

    Args:
        coef: 4 elements
    """
    def __init__(
        self,
        coef: list[float64] | list[float] = None,
    ):
        self.coef: list[float64] | list[float]

