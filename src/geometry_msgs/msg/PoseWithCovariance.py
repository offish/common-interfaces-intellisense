# flake8: noqa
from common_interfaces.base_types import *
from . import Pose

from typing import Any


class PoseWithCovariance:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PoseWithCovariance.msg

    Args:
        pose: No information
        covariance: 36 elements
    """
    def __init__(
        self,
        pose: Pose | Any = None,
        covariance: list[float64] | list[float] = None,
    ):
        self.pose: Pose | Any
        self.covariance: list[float64] | list[float]

