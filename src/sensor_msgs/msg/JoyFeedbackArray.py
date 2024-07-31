# flake8: noqa
from common_interfaces.base_types import *
from . import JoyFeedback

from typing import Any


class JoyFeedbackArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/JoyFeedbackArray.msg

    Args:
        array: No information
    """
    def __init__(
        self,
        array: list[JoyFeedback] | list[Any] = None,
    ):
        self.array: list[JoyFeedback] | list[Any]

