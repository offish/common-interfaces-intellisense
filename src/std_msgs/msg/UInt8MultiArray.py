# flake8: noqa
from common_interfaces.base_types import *
from . import MultiArrayLayout

from typing import Any


class UInt8MultiArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/UInt8MultiArray.msg

    Args:
        layout: No information
        data: No information
    """
    def __init__(
        self,
        layout: MultiArrayLayout | Any = None,
        data: list[uint8] | list[int] = None,
    ):
        self.layout: MultiArrayLayout | Any
        self.data: list[uint8] | list[int]

