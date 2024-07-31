# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import AccelWithCovariance

from typing import Any


class AccelWithCovarianceStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/AccelWithCovarianceStamped.msg

    Args:
        header: No information
        accel: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        accel: AccelWithCovariance | Any = None,
    ):
        self.header: Header | Any
        self.accel: AccelWithCovariance | Any

