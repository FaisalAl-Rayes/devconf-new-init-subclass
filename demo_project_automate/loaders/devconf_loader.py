# -*- coding: utf-8 -*-
"""DevConf File Loader."""

import pathlib

from .loader_baseclass import Loader


# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name, import-error
class DevConfLoader(Loader, file_extension=".devconf"):
    """DevConf file loader that loads the data from a .devconf file."""

    def load(self, file_location: pathlib.Path) -> str:
        """Load the CSV file into a DataFrame then makes necessary adjustments.

        :param file_location: the path of the devconf file.
        :return: the value of the file.
        """
        with open(file_location, mode="r", encoding="utf-8") as devconf_file:
            content: str = devconf_file.read()
            loaded_file = content.replace("CODE", "I am inside a .devconf file")
            return loaded_file
