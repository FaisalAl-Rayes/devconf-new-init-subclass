# -*- coding: utf-8 -*-
"""CSV File Loader."""

import pathlib

from .loader_baseclass import ALoader


# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class CsvLoader(ALoader):
    """CSV file loader that loads the data from a .csv file."""

    def load(self, file_location: pathlib.Path) -> str:
        """Load the CSV file into a DataFrame then makes necessary adjustments.

        :param file_location: the path of the CSV file.
        :return: the value of the file.
        """
        with open(file_location, mode="r", encoding="utf-8") as csv_file:
            content: str = csv_file.read()
            loaded_file = content.replace("CODE", "I am inside a .csv file")
            return loaded_file
