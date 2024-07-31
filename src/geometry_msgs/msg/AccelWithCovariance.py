# flake8: noqa
from common_interfaces.base_types import *
from . import Accel

from typing import Any


class AccelWithCovariance:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/AccelWithCovariance.msg

    Args:
        accel: No information
        covariance: 36 elements
    """
    def __init__(
        self,
        accel: Accel | Any = None,
        covariance: list[float64] | list[float] = None,
    ):
        self.accel: Accel | Any
        self.covariance: list[float64] | list[float]

