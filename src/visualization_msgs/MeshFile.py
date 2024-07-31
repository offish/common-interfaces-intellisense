# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class MeshFile:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/MeshFile.msg

    Args:
        filename: No information
        data: No information
    """
    def __init__(
        self,
        filename: string | str = None,
        data: list[uint8] | list[int] = None,
    ):
        self.filename: string | str
        self.data: list[uint8] | list[int]

