# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from geometry_msgs.msg import Pose

from typing import Any


class InteractiveMarkerPose:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarkerPose.msg

    Args:
        header: No information
        pose: No information
        name: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        pose: Pose | Any = None,
        name: string | str = None,
    ):
        self.header: Header | Any
        self.pose: Pose | Any
        self.name: string | str

