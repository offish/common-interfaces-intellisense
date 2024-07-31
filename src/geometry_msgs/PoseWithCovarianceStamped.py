# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import PoseWithCovariance

from typing import Any


class PoseWithCovarianceStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PoseWithCovarianceStamped.msg

    Args:
        header: No information
        pose: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        pose: PoseWithCovariance | Any = None,
    ):
        self.header: Header | Any
        self.pose: PoseWithCovariance | Any

