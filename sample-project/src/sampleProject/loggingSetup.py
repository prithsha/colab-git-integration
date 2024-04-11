import logging
import os
from logging.handlers import RotatingFileHandler
from sampleProject.common import constant

_app_log_file = "application.log"

def get_app_log_path():
    return os.path.join(os.getcwd(),_app_log_file)

# create file handler which logs even debug messages. 10 MB (10485760) File handler
fh = RotatingFileHandler(get_app_log_path(), maxBytes=10485760, backupCount=5)
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(name)s\t%(funcName)s\t%(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger = logging.getLogger(constant.APP_NAME)
logger.setLevel(logging.INFO)
logger.addHandler(ch)
logger.addHandler(fh)
logger.debug('Logger printing Debug configuration. Disable DEBUG level in production')
logger.info('SCT logging configuration done')

