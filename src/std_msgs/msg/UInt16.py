# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class UInt16:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/UInt16.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: uint16 | int = None,
    ):
        self.data: uint16 | int

