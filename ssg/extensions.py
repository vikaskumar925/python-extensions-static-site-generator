import sys
import importlib
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(directory)
    importlib.import_module(name)
    sys.path.pop()


def load_directory(directory):
    for path in directory.rglob(".py"):
        load_module(directory.as_posix(), path.stem)


def load_bundled():
    directory = Path(__file__).parent
    load_directory(directory)
