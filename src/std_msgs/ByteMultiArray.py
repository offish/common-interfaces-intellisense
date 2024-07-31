# flake8: noqa
from ..common_interfaces.base_types import *
from . import MultiArrayLayout

from typing import Any


class ByteMultiArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/ByteMultiArray.msg

    Args:
        layout: No information
        data: No information
    """
    def __init__(
        self,
        layout: MultiArrayLayout | Any = None,
        data: list[byte] | list[Any] = None,
    ):
        self.layout: MultiArrayLayout | Any
        self.data: list[byte] | list[Any]

