# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Vector3

from typing import Any


class MagneticField:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/MagneticField.msg

    Args:
        header: No information
        magnetic_field: No information
        magnetic_field_covariance: 9 elements
    """
    def __init__(
        self,
        header: Header | Any = None,
        magnetic_field: Vector3 | Any = None,
        magnetic_field_covariance: list[float64] | list[float] = None,
    ):
        self.header: Header | Any
        self.magnetic_field: Vector3 | Any
        self.magnetic_field_covariance: list[float64] | list[float]

