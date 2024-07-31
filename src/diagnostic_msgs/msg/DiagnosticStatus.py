# flake8: noqa
from common_interfaces.base_types import *
from . import KeyValue

from typing import Any


class DiagnosticStatus:
    """
    https://github.com/ros2/common_interfaces/blob/humble/diagnostic_msgs/msg/DiagnosticStatus.msg

    Args:
        OK: No information
        WARN: No information
        ERROR: No information
        STALE: No information
        level: No information
        name: No information
        message: No information
        hardware_id: No information
        values: No information
    """
    def __init__(
        self,
        OK: byte | bytes = None,
        WARN: byte | bytes = None,
        ERROR: byte | bytes = None,
        STALE: byte | bytes = None,
        level: byte | bytes = None,
        name: string | str = None,
        message: string | str = None,
        hardware_id: string | str = None,
        values: list[KeyValue] | list[Any] = None,
    ):
        self.OK: byte | bytes
        self.WARN: byte | bytes
        self.ERROR: byte | bytes
        self.STALE: byte | bytes
        self.level: byte | bytes
        self.name: string | str
        self.message: string | str
        self.hardware_id: string | str
        self.values: list[KeyValue] | list[Any]

