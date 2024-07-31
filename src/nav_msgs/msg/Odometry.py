# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from geometry_msgs.msg import PoseWithCovariance
from geometry_msgs.msg import TwistWithCovariance

from typing import Any


class Odometry:
    """
    https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/Odometry.msg

    Args:
        header: No information
        child_frame_id: No information
        pose: No information
        twist: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        child_frame_id: string | str = None,
        pose: PoseWithCovariance | Any = None,
        twist: TwistWithCovariance | Any = None,
    ):
        self.header: Header | Any
        self.child_frame_id: string | str
        self.pose: PoseWithCovariance | Any
        self.twist: TwistWithCovariance | Any

