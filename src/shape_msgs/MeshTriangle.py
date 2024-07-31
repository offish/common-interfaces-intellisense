# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class MeshTriangle:
    """
    https://github.com/ros2/common_interfaces/blob/humble/shape_msgs/msg/MeshTriangle.msg

    Args:
        vertex_indices: 3 elements
    """
    def __init__(
        self,
        vertex_indices: list[uint32] | list[int] = None,
    ):
        self.vertex_indices: list[uint32] | list[int]

