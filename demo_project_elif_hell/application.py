"""ELIF HELL"""

# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name, import-error
import pathlib

from loaders import loader_baseclass
from loaders import csv_loader
from loaders import devconf_loader
from loaders import ext1_loader


if __name__ == "__main__":
    file_path = pathlib.Path(__file__).parent.parent / "files/test_file.csv"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.ext1"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.devconf"

    print("----------------------------------------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("|      ELIF HELL      |")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

    extension: str = "".join(file_path.suffixes)

    loader: loader_baseclass.ALoader | None = None
    if extension == ".csv":
        loader = csv_loader.CsvLoader()
    elif extension == ".ext1":
        loader = ext1_loader.Ext1Loader()
    elif extension == ".devconf":
        loader = devconf_loader.DevConfLoader()
    elif loader is None:
        raise ValueError(f"The extension {extension} does not have a loader implemented.")

    print(f"Loading {file_path} ...")
    file_content = loader.load(file_location=file_path)
    print(f"Content of file:\n\n{file_content}")

    print("----------------------------------------------------------------------------------")
