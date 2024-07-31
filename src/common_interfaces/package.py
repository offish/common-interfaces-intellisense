import pathlib

from .parser import Parser
from .interface import Interface


class Package:
    def __init__(self, package_path: pathlib.Path, output_path: pathlib.Path) -> None:
        self.path = package_path
        self.output_path = output_path
        self.package_name = package_path.name
        self.msgs = []
        self.srvs = []

        if self.has_msg_folder():
            self.msgs = self.get_msgs()

        if self.has_srv_folder():
            self.srvs = self.get_srvs()

    def _get_package_path(self, folder: str) -> pathlib.Path:
        return self.path / folder

    def has_msg_folder(self) -> bool:
        msg_path = self._get_package_path("msg")
        return msg_path.exists()

    def has_srv_folder(self) -> bool:
        srv_path = self._get_package_path("srv")
        return srv_path.exists()

    def get_msgs(self) -> list[pathlib.Path]:
        msg_path = self._get_package_path("msg")
        return [i for i in msg_path.glob("*.msg")]

    def get_srvs(self) -> list[pathlib.Path]:
        srv_path = self._get_package_path("srv")
        return [i for i in srv_path.glob("*.srv")]

    def write_init(self) -> None:
        path = self.output_path / "__init__.py"

        # there were no interfaces made for this package
        if not path.parent.exists():
            return

        code = "# flake8: noqa\n"

        for msg in self.msgs:
            msg_name = msg.stem
            code += f"from .{msg_name} import {msg_name}\n"

        path.write_text(code, "utf-8")

    def build(self) -> None:

        for msg in self.msgs:
            parser = Parser(msg)
            types_and_keys = parser.get_types_and_keys()

            interface = Interface(
                self.path,
                self.output_path,
                self.package_name,
                msg.stem,
                "msg",
                types_and_keys,
            )
            interface.build()

            self.write_init()

        self.write_init()
