from __future__ import annotations

import hashlib
import os
from logging import getLogger
from os.path import basename, join, relpath
from zipfile import ZipFile


logger = getLogger("os_utils.operations")


def get_md5(file_path: str) -> str:
    md5_hash = hashlib.md5()  # noqa: S324
    with open(file_path, "rb") as file_:
        batch_size = 4096
        chunk = file_.read(batch_size)
        while chunk:
            md5_hash.update(chunk)
            chunk = file_.read(batch_size)

        return hashlib.md5(file_.read()).hexdigest()  # noqa: S324


def zip_dir(path: str, zip_file_path: str | None = None, zip_root: str | None = None) -> None:
    zip_file_path = zip_file_path or f"{path}.zip"
    zip_root = zip_root or basename(path)
    with ZipFile(zip_file_path, "w") as zip_file:
        for root, _dirs, files in os.walk(path):
            for file in files:
                file_path = join(root, file)
                try:
                    zip_file.write(file_path, join(zip_root, relpath(file_path, path)))
                except OSError:
                    logger.warning("file disappeared before it was zipped: %s", file_path)
