import os
import shutil
from logging import getLogger
from os.path import exists, isdir, isfile, islink, join
from stat import S_IWGRP, S_IWOTH, S_IWUSR, ST_MODE
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Sequence


WRITE = S_IWUSR | S_IWGRP | S_IWOTH

logger = getLogger("os_utils.path")


def clear_dir(path: str) -> None:
    delete(path)
    mkpath(path)


def delete(path: str) -> None:
    if exists(path):
        if isdir(path):
            add_permissions_to_dir_rec(path, WRITE)
            shutil.rmtree(path)
        elif isfile(path):
            add_permissions_to_path(path, WRITE)
            os.remove(path)
        elif islink(path):
            add_permissions_to_path(path, WRITE)
            os.unlink(path)


def add_permissions_to_path(path: str, permissions: int) -> None:
    os.chmod(path, os.stat(path)[ST_MODE] | permissions)


def add_permissions_to_multiple_paths(root: str, paths: Sequence[str], permissions: int) -> None:
    for path in paths:
        add_permissions_to_path(join(root, path), permissions)


def add_permissions_to_dir_rec(path: str, permissions: int) -> None:
    for root, dirs, files in os.walk(path):
        add_permissions_to_multiple_paths(root, dirs + files, permissions)


def mkpath(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except (OSError, FileExistsError):
        logger.warning(
            "Failure during creation of the path: %s, path exists already most likely",
            path,
        )
