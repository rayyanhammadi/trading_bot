import logging
import sys

from logger.telegram_handler import TELEGRAM_HANDLER

APP_LOGGER_NAME = 'trading bot'


def setup_applevel_logger(logger_name=APP_LOGGER_NAME,
                          is_debug=True,
                          file_name=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG if is_debug else logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)
    telegramh = TELEGRAM_HANDLER()
    logger.addHandler(telegramh)

    if file_name:
        fh = logging.FileHandler(file_name)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)


log = setup_applevel_logger(logger_name='futures fetcher')


def log_if_errors(logger):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception:
                logger.exception(f'{fn.__name__} call failed')

        return wrapper

    return decorator
