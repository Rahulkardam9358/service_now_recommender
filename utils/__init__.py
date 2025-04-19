from .configuration import Config
from .logger import Logger


logger = Logger().get_logger()
config = Config()


__all__ = ["config", "logger",]
