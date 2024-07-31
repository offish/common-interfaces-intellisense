# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class Range:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Range.msg

    Args:
        header: No information
        ULTRASOUND: No information
        INFRARED: No information
        radiation_type: No information
        field_of_view: No information
        min_range: No information
        max_range: No information
        range: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        ULTRASOUND: uint8 | int = None,
        INFRARED: uint8 | int = None,
        radiation_type: uint8 | int = None,
        field_of_view: float32 | float = None,
        min_range: float32 | float = None,
        max_range: float32 | float = None,
        range: float32 | float = None,
    ):
        self.header: Header | Any
        self.ULTRASOUND: uint8 | int
        self.INFRARED: uint8 | int
        self.radiation_type: uint8 | int
        self.field_of_view: float32 | float
        self.min_range: float32 | float
        self.max_range: float32 | float
        self.range: float32 | float

