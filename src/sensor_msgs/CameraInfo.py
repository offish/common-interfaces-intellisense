# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import RegionOfInterest

from typing import Any


class CameraInfo:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/CameraInfo.msg

    Args:
        header: No information
        height: No information
        width: No information
        distortion_model: No information
        d: No information
        k: 9 elements
        r: 9 elements
        p: 12 elements
        binning_x: No information
        binning_y: No information
        roi: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        height: uint32 | int = None,
        width: uint32 | int = None,
        distortion_model: string | str = None,
        d: list[float64] | list[float] = None,
        k: list[float64] | list[float] = None,
        r: list[float64] | list[float] = None,
        p: list[float64] | list[float] = None,
        binning_x: uint32 | int = None,
        binning_y: uint32 | int = None,
        roi: RegionOfInterest | Any = None,
    ):
        self.header: Header | Any
        self.height: uint32 | int
        self.width: uint32 | int
        self.distortion_model: string | str
        self.d: list[float64] | list[float]
        self.k: list[float64] | list[float]
        self.r: list[float64] | list[float]
        self.p: list[float64] | list[float]
        self.binning_x: uint32 | int
        self.binning_y: uint32 | int
        self.roi: RegionOfInterest | Any

