import pathlib


class Parser:
    def __init__(self, file: pathlib.Path):
        self.file = file

    def _read(self) -> str:
        return self.file.read_text("utf-8")

    def _parse_line(self, line: str) -> tuple[str, str] | None:
        if not line:
            return None

        if line.startswith("#"):
            return None

        data = line.split(" ")
        valid_entries = []

        for i in data:
            if not i:
                continue

            # TODO: include comment in docstring
            if "#" in i:
                break

            valid_entries.append(i)

        if not valid_entries:
            return None

        data_type = valid_entries[0]

        for i in valid_entries[1:]:
            if not i:
                continue

            data_key = i
            break

        if "=" in data_key:
            data_key = data_key.split("=")[0]

        return data_type, data_key

    def get_types_and_keys(self) -> dict[str, str]:
        content = self._read()
        lines = content.split("\n")
        result = {}

        for line in lines:
            data = self._parse_line(line)

            if data is None:
                continue

            data_type, data_key = data
            result[data_key] = data_type

        return result
