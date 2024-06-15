"""AUTOMATE"""

# pylint: disable=wildcard-import,too-few-public-methods, super-init-not-called, invalid-name, import-error
import pathlib
import pprint

from loaders import *
from loaders.loader_baseclass import ALoader, Loader


if __name__ == "__main__":

    print("\nAVAILABLE LOADERS:")
    pprint.pprint(Loader.available_loaders)

    file_path = pathlib.Path(__file__).parent.parent / "files/test_file.csv"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.ext1"
    # file_path = pathlib.Path(__file__).parent.parent / "files/test_file.devconf"

    print("--------------------------------------------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("|  AUTOMATE (HEAVEN?)  |")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

    extension: str = "".join(file_path.suffixes)          # output: .csv, .devconf, ...
    loader: ALoader = Loader(file_extension=extension)    # output: CsvLoader, DevConfLoader, ...

    print(f"The Loader is class {loader.__class__}")
    print(f"Loading {file_path} ...")

    file_content = loader.load(file_location=file_path)   # output: hello, (decoded CODE)
    print(f"Content of file:\n\n{file_content}")

    print("--------------------------------------------------------------------------------------")
