# -*- coding: utf-8 -*-
"""Module holds the Loader interface."""

from abc import ABC, abstractmethod

import pathlib


# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class ALoader(ABC):
    """Interface of a Loader."""

    @abstractmethod
    def load(self, file_location: pathlib.Path) -> str:
        """Load the preprocessed data."""
