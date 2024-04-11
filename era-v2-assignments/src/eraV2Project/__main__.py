"""Access Controller APIs."""

__version__ = '0.1.0'

# from sampleProject.models.model1 import ModelOne

# x = ModelOne()
# print(x.get_number())
# print(x.get_version())

print("From __main__")
import sampleProject.loggingSetup
from sampleProject.common import constant
import logging

logger = logging.getLogger(constant.APP_NAME).getChild(__name__)

logger.info(f"Main execution started. Log file : {sampleProject.loggingSetup.get_app_log_path()}")


