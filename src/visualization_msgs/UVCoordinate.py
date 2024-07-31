# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class UVCoordinate:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/UVCoordinate.msg

    Args:
        u: No information
        v: No information
    """
    def __init__(
        self,
        u: float32 | float = None,
        v: float32 | float = None,
    ):
        self.u: float32 | float
        self.v: float32 | float

