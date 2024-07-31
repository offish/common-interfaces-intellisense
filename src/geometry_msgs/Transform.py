# flake8: noqa
from ..common_interfaces.base_types import *
from . import Vector3
from . import Quaternion

from typing import Any


class Transform:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Transform.msg

    Args:
        translation: No information
        rotation: No information
    """
    def __init__(
        self,
        translation: Vector3 | Any = None,
        rotation: Quaternion | Any = None,
    ):
        self.translation: Vector3 | Any
        self.rotation: Quaternion | Any

