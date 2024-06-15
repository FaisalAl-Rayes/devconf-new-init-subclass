# -*- coding: utf-8 -*-
"""Module holds the Loader interface and baseclass."""

from abc import ABC, abstractmethod

import pathlib
from typing import Any


# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name, import-error
class ALoader(ABC):
    """Interface of a Loader."""

    @abstractmethod
    def load(self, file_location: pathlib.Path) -> str:
        """Load the preprocessed data."""


class Loader(ALoader):
    """Baseclass of a Loader."""

    available_loaders: dict[str, Any] = {}

    def __init_subclass__(cls, file_extension: str):
        """Initialize subclass."""
        if not file_extension:
            raise ValueError("The concrete loader class must have a file_extension that it can load.")
        super().__init_subclass__()
        cls.available_loaders[file_extension] = cls
        print(f"Done mapping the name ({file_extension}) to class ({cls})")

    def __new__(cls, file_extension: str, **attrs):
        """Create a new object."""
        cls.attrs = attrs
        try:
            subclass = cls.available_loaders[file_extension]
            obj = object.__new__(subclass)
        except KeyError:
            raise NotImplementedError(
                f'File type of "{file_extension}" does not have a loader implemented.'
            )
        return obj

    def __init__(self, file_extension: str, **attributes: Any):
        """Initialize the loader class."""
        self.file_extension = file_extension
        _ = [setattr(self, attr, value) for attr, value in attributes.items()]

    def load(self, file_location: pathlib.Path) -> str:
        """Load the preprocessed data."""
        raise NotImplementedError(
            f'The loader "{self.__class__.__name__}" does not have a .load method implemented.'
        )
