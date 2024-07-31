# flake8: noqa
from ..common_interfaces.base_types import *
from . import Twist

from typing import Any


class TwistWithCovariance:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/TwistWithCovariance.msg

    Args:
        twist: No information
        covariance: 36 elements
    """
    def __init__(
        self,
        twist: Twist | Any = None,
        covariance: list[float64] | list[float] = None,
    ):
        self.twist: Twist | Any
        self.covariance: list[float64] | list[float]

