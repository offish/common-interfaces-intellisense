INTERFACE_URL = "https://github.com/ros2/common_interfaces/blob/{}/{}/msg/{}"
INTERFACE_CODE = """# flake8: noqa
from common_interfaces.base_types import *
{imports}
from typing import Any


class {interface_name}:
    \"\"\"
    {interface_url}

    Args:{docstrings}
    \"\"\"
    def __init__(
        self,{args}
    ):
{attrs}
"""
