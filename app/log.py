"""
logging.
"""

import logging
from config.config import Config

# setup loggers
# logging.config.fileConfig(Config.LOG_FILE, disable_existing_loggers=False)
# logging.basicConfig(filename=Config.LOG_FILE, level=logging.DEBUG)

# get root logger
logger = logging.getLogger('app')
