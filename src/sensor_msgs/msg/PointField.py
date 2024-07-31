# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class PointField:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/PointField.msg

    Args:
        INT8: No information
        UINT8: No information
        INT16: No information
        UINT16: No information
        INT32: No information
        UINT32: No information
        FLOAT32: No information
        FLOAT64: No information
        name: No information
        offset: No information
        datatype: No information
        count: No information
    """
    def __init__(
        self,
        INT8: uint8 | int = None,
        UINT8: uint8 | int = None,
        INT16: uint8 | int = None,
        UINT16: uint8 | int = None,
        INT32: uint8 | int = None,
        UINT32: uint8 | int = None,
        FLOAT32: uint8 | int = None,
        FLOAT64: uint8 | int = None,
        name: string | str = None,
        offset: uint32 | int = None,
        datatype: uint8 | int = None,
        count: uint32 | int = None,
    ):
        self.INT8: uint8 | int
        self.UINT8: uint8 | int
        self.INT16: uint8 | int
        self.UINT16: uint8 | int
        self.INT32: uint8 | int
        self.UINT32: uint8 | int
        self.FLOAT32: uint8 | int
        self.FLOAT64: uint8 | int
        self.name: string | str
        self.offset: uint32 | int
        self.datatype: uint8 | int
        self.count: uint32 | int

