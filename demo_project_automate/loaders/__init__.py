"""Set a meaningfull wildcard."""

import os
import pathlib


__all__ = [
    pathlib.Path(module).stem
    for module in os.listdir(pathlib.Path(__file__).parent)
    if module.endswith("_loader.py") or module.endswith("_baseclass.py")
]
