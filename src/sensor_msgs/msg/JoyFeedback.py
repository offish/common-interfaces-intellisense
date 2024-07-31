# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class JoyFeedback:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/JoyFeedback.msg

    Args:
        TYPE_LED: No information
        TYPE_RUMBLE: No information
        TYPE_BUZZER: No information
        type: No information
        id: No information
        intensity: No information
    """
    def __init__(
        self,
        TYPE_LED: uint8 | int = None,
        TYPE_RUMBLE: uint8 | int = None,
        TYPE_BUZZER: uint8 | int = None,
        type: uint8 | int = None,
        id: uint8 | int = None,
        intensity: float32 | float = None,
    ):
        self.TYPE_LED: uint8 | int
        self.TYPE_RUMBLE: uint8 | int
        self.TYPE_BUZZER: uint8 | int
        self.type: uint8 | int
        self.id: uint8 | int
        self.intensity: float32 | float

