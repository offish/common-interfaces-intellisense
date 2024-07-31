# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class Int64:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Int64.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: int64 | int = None,
    ):
        self.data: int64 | int

