# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class LaserEcho:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/LaserEcho.msg

    Args:
        echoes: No information
    """
    def __init__(
        self,
        echoes: list[float32] | list[float] = None,
    ):
        self.echoes: list[float32] | list[float]

