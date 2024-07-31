# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class LaserScan:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/LaserScan.msg

    Args:
        header: No information
        angle_min: No information
        angle_max: No information
        angle_increment: No information
        time_increment: No information
        scan_time: No information
        range_min: No information
        range_max: No information
        ranges: No information
        intensities: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        angle_min: float32 | float = None,
        angle_max: float32 | float = None,
        angle_increment: float32 | float = None,
        time_increment: float32 | float = None,
        scan_time: float32 | float = None,
        range_min: float32 | float = None,
        range_max: float32 | float = None,
        ranges: list[float32] | list[float] = None,
        intensities: list[float32] | list[float] = None,
    ):
        self.header: Header | Any
        self.angle_min: float32 | float
        self.angle_max: float32 | float
        self.angle_increment: float32 | float
        self.time_increment: float32 | float
        self.scan_time: float32 | float
        self.range_min: float32 | float
        self.range_max: float32 | float
        self.ranges: list[float32] | list[float]
        self.intensities: list[float32] | list[float]

