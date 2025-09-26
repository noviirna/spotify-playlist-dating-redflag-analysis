import os

from ..constant.constant import (FileWriter)


def write_output_to_json(filename: str, json_string: str) -> None:
    with (open(os.path.join(filename + ".json"), FileWriter.METHOD_TYPE_WRITE,
               encoding=FileWriter.ENCODING_UTF_8) as file):
        file.write(json_string)


def write_output_to_markdown(filename: str, string: str) -> None:
    with (open(os.path.join(filename + ".md"), FileWriter.METHOD_TYPE_WRITE,
               encoding=FileWriter.ENCODING_UTF_8) as file):
        file.write(string)
