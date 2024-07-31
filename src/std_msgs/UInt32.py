# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class UInt32:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/UInt32.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: uint32 | int = None,
    ):
        self.data: uint32 | int

