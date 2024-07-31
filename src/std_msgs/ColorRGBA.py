# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class ColorRGBA:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/ColorRGBA.msg

    Args:
        r: No information
        g: No information
        b: No information
        a: No information
    """
    def __init__(
        self,
        r: float32 | float = None,
        g: float32 | float = None,
        b: float32 | float = None,
        a: float32 | float = None,
    ):
        self.r: float32 | float
        self.g: float32 | float
        self.b: float32 | float
        self.a: float32 | float

