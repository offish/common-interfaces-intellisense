# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import Twist

from typing import Any


class VelocityStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/VelocityStamped.msg

    Args:
        header: No information
        body_frame_id: No information
        reference_frame_id: No information
        velocity: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        body_frame_id: string | str = None,
        reference_frame_id: string | str = None,
        velocity: Twist | Any = None,
    ):
        self.header: Header | Any
        self.body_frame_id: string | str
        self.reference_frame_id: string | str
        self.velocity: Twist | Any

