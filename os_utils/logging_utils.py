import logging
import logging.handlers
import sys
from contextlib import contextmanager
from datetime import UTC, datetime
from os import getcwd
from os.path import join
from typing import IO, TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Generator


LOGGING_FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
DATE_FORMAT = "[%Y-%m-%d %H:%M:%S]"

logger = logging.getLogger("os_utils.logging_utils")
logging.getLogger().level = logging.DEBUG
TEN_MB = 10 * (1024**2)


def configure_stream_logger(
    stream: IO[str] = sys.stdout, level: str = "DEBUG", track_configured_loggers: bool = True
) -> None:
    level_int = logging.getLevelName(level)
    if track_configured_loggers:
        for handler in logging.root.handlers:
            if (
                isinstance(handler, logging.StreamHandler)
                and handler.stream == stream
                and handler.level == level_int
            ):
                return

    stream_handler = logging.StreamHandler(stream=stream)
    stream_handler.level = level_int
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    stream_handler.setFormatter(formatter)
    logging.getLogger().addHandler(stream_handler)


def configure_file_logger(
    filename: str = "app.log", level: str = "DEBUG", rotate_file: bool = True
) -> None:
    file_path = join(getcwd(), filename)
    file_handler = logging.FileHandler(filename=file_path)
    file_handler.level = logging.getLevelName(level)
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
    if rotate_file:
        open(file_path, "w").close()


def configure_file_and_stream_logger(
    stream: IO[str] = sys.stdout,
    filename: str = "app.log",
    level: str = "DEBUG",
    rotate_file: bool = True,
) -> None:
    configure_stream_logger(stream, level)
    configure_file_logger(filename, level, rotate_file)


def configure_file_rotate_handler(
    filename: str = "app.log", level: str = "DEBUG", max_bytes: int = TEN_MB
) -> None:
    file_path = join(getcwd(), filename)
    file_handler = logging.handlers.RotatingFileHandler(
        filename=file_path, maxBytes=max_bytes, backupCount=3
    )
    file_handler.level = logging.getLevelName(level)
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)


@contextmanager
def timeit() -> Generator[None]:
    start_time = datetime.now(tz=UTC)
    logger.info("START TIME: %s", start_time)
    yield
    logger.info("TIME SPENT: %s", (datetime.now(tz=UTC) - start_time))


@contextmanager
def timeit_with_context(context_name: str) -> Generator[None]:
    start_time = datetime.now(tz=UTC)
    yield
    logger.info(
        "TIME SPENT for %s: %s",
        context_name,
        datetime.now(tz=UTC) - start_time,
    )
