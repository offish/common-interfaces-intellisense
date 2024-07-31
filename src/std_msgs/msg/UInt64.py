# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class UInt64:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/UInt64.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: uint64 | int = None,
    ):
        self.data: uint64 | int

