# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class MultiArrayDimension:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/MultiArrayDimension.msg

    Args:
        label: No information
        size: No information
        stride: No information
    """
    def __init__(
        self,
        label: string | str = None,
        size: uint32 | int = None,
        stride: uint32 | int = None,
    ):
        self.label: string | str
        self.size: uint32 | int
        self.stride: uint32 | int

