import logging
import logging.handlers
import sys
from contextlib import contextmanager
from datetime import datetime
from os import getcwd
from os.path import join

LOGGING_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
DATE_FORMAT = '[%Y-%m-%d %H:%M:%S]'

logger = logging.getLogger()
logger.level = logging.DEBUG
TEN_MB = 10 * (1024 ** 2)


def configure_stream_logger(stream=sys.stdout, level='DEBUG', track_configured_loggers=True):
    level = logging.getLevelName(level)
    if track_configured_loggers:
        for handler in logging.root.handlers:
            if isinstance(handler, logging.StreamHandler) and handler.stream == stream \
                    and handler.level == level:
                return

    stream_handler = logging.StreamHandler(stream=stream)
    stream_handler.level = level
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    stream_handler.setFormatter(formatter)
    logging.getLogger().addHandler(stream_handler)


def configure_file_logger(filename='app.log', level='DEBUG', rotate_file=True):
    file_path = join(getcwd(), filename)
    file_handler = logging.FileHandler(filename=file_path)
    file_handler.level = logging.getLevelName(level)
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
    if rotate_file:
        open(file_path, 'w').close()


def configure_file_and_stream_logger(stream=sys.stdout, filename='app.log', level='DEBUG', rotate_file=True):
    configure_stream_logger(stream, level)
    configure_file_logger(filename, level, rotate_file)


def configure_file_rotate_handler(filename='app.log', level='DEBUG'):
    file_path = join(getcwd(), filename)
    file_handler = logging.handlers.RotatingFileHandler(filename=file_path,
                                                        maxBytes=TEN_MB, backupCount=3)
    file_handler.level = logging.getLevelName(level)
    formatter = logging.Formatter(datefmt=DATE_FORMAT, fmt=LOGGING_FORMAT)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)


@contextmanager
def timeit():
    start_time = datetime.now()
    logger.info('START TIME: %s', start_time)
    yield
    logger.info('TIME SPENT: %s', (datetime.now() - start_time))


def timeit_with_context(context_name):
    start_time = datetime.now()
    yield
    logger.info('TIME SPENT for {}: {}'.format(context_name, datetime.now() - start_time))
