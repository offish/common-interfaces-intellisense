from .package import Package

import pathlib


class BuildInterfaces:
    def __init__(self):
        self.base_path = pathlib.Path(__file__).parent.parent.parent
        self.packages_path = self.base_path / "humble"

    def get_packages(self) -> list[pathlib.Path]:
        return [i for i in self.packages_path.glob("*_*")]

    def get_output_folder(self, package_name: str) -> pathlib.Path:
        return self.base_path / "src" / package_name

    def delete_built_files(self) -> None:
        path = self.base_path / "src"

        for i in path.glob("*_*"):
            # .egg-info or pycache
            if "." in i.name or "__" in i.name:
                continue

            if i.name in ["common_interfaces", "base_types", "builtin_interfaces"]:
                continue

            for file in i.glob("*.py"):
                file.unlink()

            i.rmdir()

    def build(self) -> None:
        self.delete_built_files()

        for package_path in self.get_packages():
            output_path = self.get_output_folder(package_path.name)

            package = Package(package_path, output_path)
            package.build()

            # TODO: add services
            # if self.has_srv_folder(package):
            #     print("  srvs:")
            #     for srv in self.get_srvs(package):
            #         print(f"    {srv}")
