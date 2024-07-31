# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import PointField

from typing import Any


class PointCloud2:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/PointCloud2.msg

    Args:
        header: No information
        height: No information
        width: No information
        fields: No information
        is_bigendian: No information
        point_step: No information
        row_step: No information
        data: No information
        is_dense: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        height: uint32 | int = None,
        width: uint32 | int = None,
        fields: list[PointField] | list[int] = None,
        is_bigendian: bool = None,
        point_step: uint32 | int = None,
        row_step: uint32 | int = None,
        data: list[uint8] | list[int] = None,
        is_dense: bool = None,
    ):
        self.header: Header | Any
        self.height: uint32 | int
        self.width: uint32 | int
        self.fields: list[PointField] | list[int]
        self.is_bigendian: bool
        self.point_step: uint32 | int
        self.row_step: uint32 | int
        self.data: list[uint8] | list[int]
        self.is_dense: bool

