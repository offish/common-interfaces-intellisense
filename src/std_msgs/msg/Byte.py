# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Byte:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Byte.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: byte | bytes = None,
    ):
        self.data: byte | bytes

