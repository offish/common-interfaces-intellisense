# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import DiagnosticStatus

from typing import Any


class DiagnosticArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/diagnostic_msgs/msg/DiagnosticArray.msg

    Args:
        header: No information
        status: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        status: list[DiagnosticStatus] | list[Any] = None,
    ):
        self.header: Header | Any
        self.status: list[DiagnosticStatus] | list[Any]

