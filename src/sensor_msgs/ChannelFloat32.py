# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class ChannelFloat32:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/ChannelFloat32.msg

    Args:
        name: No information
        values: No information
    """
    def __init__(
        self,
        name: string | str = None,
        values: list[float32] | list[float] = None,
    ):
        self.name: string | str
        self.values: list[float32] | list[float]

