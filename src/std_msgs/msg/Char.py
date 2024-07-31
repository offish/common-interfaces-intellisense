# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Char:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Char.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: char | str = None,
    ):
        self.data: char | str

