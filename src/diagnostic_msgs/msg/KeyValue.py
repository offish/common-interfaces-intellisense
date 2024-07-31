# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class KeyValue:
    """
    https://github.com/ros2/common_interfaces/blob/humble/diagnostic_msgs/msg/KeyValue.msg

    Args:
        key: No information
        value: No information
    """
    def __init__(
        self,
        key: string | str = None,
        value: string | str = None,
    ):
        self.key: string | str
        self.value: string | str

