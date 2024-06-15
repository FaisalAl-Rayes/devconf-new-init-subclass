"""BETTER HELL"""

# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name, import-error
import pathlib
import typing

from loaders import loader_baseclass
from loaders import csv_loader
from loaders import devconf_loader
from loaders import ext1_loader

LOADER_LOOKUP: dict[str, typing.Any] = {
    ".csv": csv_loader.CsvLoader,
    ".ext1": ext1_loader.Ext1Loader,
    ".devconf": devconf_loader.DevConfLoader,
}

if __name__ == "__main__":
    file_path = pathlib.Path(__file__).parent.parent / "files/test_file.csv"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.ext1"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.devconf"

    print("----------------------------------------------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("|     BETTER HELL     |")
    print("~~~~~~~~~~~~~~~~~~~~~~~")


    extension: str = "".join(file_path.suffixes)


    try:
        loader: loader_baseclass.ALoader = LOADER_LOOKUP[extension]()
    except KeyError as exp:
        exp.add_note(f"File type ({extension}) does not have a loader implemented.")
        raise exp

    print(f"Loading {file_path} ...")
    file_content = loader.load(file_location=file_path)
    print(f"Content of file:\n\n{file_content}")

    print("----------------------------------------------------------------------------------------")
