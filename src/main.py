import os
import logging
import h5py

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
PORT = os.getenv("APP_PORT", "9090")

LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL, format='[%(levelname)s][%(asctime)s][%(threadName)s][%(name)s] %(message)s')

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Hydroserving keras runtime")
    h5py.
