# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import MapMetaData

from typing import Any


class OccupancyGrid:
    """
    https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/OccupancyGrid.msg

    Args:
        header: No information
        info: No information
        data: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        info: MapMetaData | Any = None,
        data: list[int8] | list[int] = None,
    ):
        self.header: Header | Any
        self.info: MapMetaData | Any
        self.data: list[int8] | list[int]

