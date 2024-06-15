# -*- coding: utf-8 -*-
"""Ext1 File Loader."""

import pathlib

from .loader_baseclass import ALoader


# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class Ext1Loader(ALoader):
    """Ext1 file loader that loads the data from a .ext1 file"""

    def load(self, file_location: pathlib.Path) -> str:
        """Load the Ext1 file.

        :param file_location: the path of the Ext1 file.
        :return: the value of the file.
        """
        with open(file_location, mode="r", encoding="utf-8") as ext1_file:
            content: str = ext1_file.read()
            loaded_file = content.replace("CODE", "I am inside a .ext1 file")
            return loaded_file
