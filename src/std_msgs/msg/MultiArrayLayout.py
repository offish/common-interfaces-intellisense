# flake8: noqa
from common_interfaces.base_types import *
from . import MultiArrayDimension

from typing import Any


class MultiArrayLayout:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/MultiArrayLayout.msg

    Args:
        dim: No information
        data_offset: No information
    """
    def __init__(
        self,
        dim: list[MultiArrayDimension] | list[Any] = None,
        data_offset: uint32 | int = None,
    ):
        self.dim: list[MultiArrayDimension] | list[Any]
        self.data_offset: uint32 | int

