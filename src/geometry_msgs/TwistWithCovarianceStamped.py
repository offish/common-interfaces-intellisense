# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import TwistWithCovariance

from typing import Any


class TwistWithCovarianceStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/TwistWithCovarianceStamped.msg

    Args:
        header: No information
        twist: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        twist: TwistWithCovariance | Any = None,
    ):
        self.header: Header | Any
        self.twist: TwistWithCovariance | Any

