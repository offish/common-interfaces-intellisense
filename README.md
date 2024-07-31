# common-interfaces-intellisense
Get intellisense for ROS 2 messages. Services are not supported. 
This is a only intended to be used for intellisense purposes.
Useful if developing on another system than where ROS 2 is available (Docker for example).
Code within this package is NOT intended to be ran.

## Installation
```bash
pip install common-interfaces-intellisense
```

## Usage
```python
from geometry_msgs.msg import Quaternion
from std_msgs.msg import String

# will now get intellisense
msg = Quaternion()

# or
msg = String(data="my string")
```

Here is an example of a generated class:

[`sensor_msgs/msg/CameraInfo.py`](/src/sensor_msgs/msg/CameraInfo.py)

```python
# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
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

```

## Build
```python
from common_interfaces.build import BuildInterfaces

BuildInterfaces().build()
```
