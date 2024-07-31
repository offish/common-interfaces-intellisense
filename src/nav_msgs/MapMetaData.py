# flake8: noqa
from ..common_interfaces.base_types import *
from ..builtin_interfaces import Time
from ..geometry_msgs import Pose

from typing import Any


class MapMetaData:
    """
    https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/MapMetaData.msg

    Args:
        map_load_time: No information
        resolution: No information
        width: No information
        height: No information
        origin: No information
    """
    def __init__(
        self,
        map_load_time: Time | int = None,
        resolution: float32 | float = None,
        width: uint32 | int = None,
        height: uint32 | int = None,
        origin: Pose | Any = None,
    ):
        self.map_load_time: Time | int
        self.resolution: float32 | float
        self.width: uint32 | int
        self.height: uint32 | int
        self.origin: Pose | Any

