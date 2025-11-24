import logging
import logging.config

from config import Config

logging.config.fileConfig(Config.LOG_CONFIG)

logger = logging.getLogger("__name__")
