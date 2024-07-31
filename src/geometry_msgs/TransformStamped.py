# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import Transform

from typing import Any


class TransformStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/TransformStamped.msg

    Args:
        header: No information
        child_frame_id: No information
        transform: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        child_frame_id: string | str = None,
        transform: Transform | Any = None,
    ):
        self.header: Header | Any
        self.child_frame_id: string | str
        self.transform: Transform | Any

