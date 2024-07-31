# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from sensor_msgs.msg import RegionOfInterest

from typing import Any


class DisparityImage:
    """
    https://github.com/ros2/common_interfaces/blob/humble/stereo_msgs/msg/DisparityImage.msg

    Args:
        header: No information
        image: No information
        f: No information
        t: No information
        valid_window: No information
        min_disparity: No information
        max_disparity: No information
        delta_d: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        image: Image | Any = None,
        f: float32 | float = None,
        t: float32 | float = None,
        valid_window: RegionOfInterest | Any = None,
        min_disparity: float32 | float = None,
        max_disparity: float32 | float = None,
        delta_d: float32 | float = None,
    ):
        self.header: Header | Any
        self.image: Image | Any
        self.f: float32 | float
        self.t: float32 | float
        self.valid_window: RegionOfInterest | Any
        self.min_disparity: float32 | float
        self.max_disparity: float32 | float
        self.delta_d: float32 | float

