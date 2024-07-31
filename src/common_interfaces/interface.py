import pathlib

from .constants import INTERFACE_URL, INTERFACE_CODE
from .base_types import __all__


class Interface:
    def __init__(
        self,
        package_path: pathlib.Path,
        output_path: pathlib.Path,
        package_name: str,
        interface_name: str,
        interface_type: str,
        types_and_keys: dict[str, str],
        branch: str = "humble",
    ):
        self.package_path = package_path
        self.package_name = package_name
        self.interface_name = interface_name
        self.interface_type = interface_type
        self.path = output_path / f"{interface_name}.py"
        self.data = []

        data = types_and_keys

        for key in data:
            imports, interface, docstring = self._get_key_data(data[key], key)
            python_type = self._get_python_type(data[key])
            self.data.append(
                (
                    key,
                    imports,
                    interface,
                    python_type,
                    docstring,
                )
            )

        self.branch = branch

    def _get_python_type(self, data_type: str) -> str:
        if data_type == "string":
            return "str"
        if data_type == "char":
            return "str"

        if data_type == "byte":
            return "bytes"

        if data_type == "bool":
            return "bool"

        if "int" in data_type:
            return "int"

        if "float" in data_type:
            return "float"

        return "Any"

    @staticmethod
    def _get_key_data(key: str, actual_key: str) -> tuple[str, str, str]:
        was_list = False
        list_size = None
        imports = ""
        interface = key

        if "[" in key:
            was_list = True
            start_index = key.index("[")
            end_index = key.index("]")

            if end_index - start_index > 1:
                content = key[start_index + 1 : end_index]

                if content.isdigit():
                    list_size = int(key[start_index + 1 : end_index])

            interface = key[:start_index]

        if "/" in key:
            package, import_interface = key.split("/")

            if interface:
                interface = interface.split("/")[-1]

            if not interface:
                interface = import_interface

            imports += f"from ..{package} import {interface}\n"
        else:
            if interface not in __all__ + ["bool"]:
                imports += f"from . import {interface}\n"

        if was_list:
            interface = f"list[{interface}]"

        docstring = "\n" + " " * 8

        if list_size:
            docstring += f"{actual_key}: {list_size} elements"
        else:
            docstring += f"{actual_key}: No information"

        return imports, interface, docstring

    def _get_url(self) -> str:
        return INTERFACE_URL.format(
            self.branch, self.package_name, self.interface_name + ".msg"
        )

    def build(self) -> None:
        imports = ""
        args = ""
        attrs = ""
        docstrings = ""

        for i in self.data:
            key, new_imports, interface, python_type, docstring = i

            imports += new_imports
            docstrings += docstring

            types = ""

            if "list" == interface[:4]:
                python_type = f"list[{python_type}]"

            if interface == python_type:
                types = interface
            else:
                types = f"{interface} | {python_type}"

            args += "\n" + " " * 8 + f"{key}: {types} = None,"
            attrs += " " * 8 + f"self.{key}: {types}\n"

        if self.interface_name == "Empty":
            imports = ""
            args = ""
            attrs = " " * 8 + "pass"
            docstrings = ""

        code = INTERFACE_CODE.format(
            imports=imports,
            interface_name=self.interface_name,
            interface_url=self._get_url(),
            docstrings=docstrings,
            args=args,
            attrs=attrs,
        )

        parent = self.path.parent

        if not parent.exists():
            parent.mkdir()

        self.path.write_text(code, "utf-8")
