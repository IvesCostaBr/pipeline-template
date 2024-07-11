import time
import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def exec(data):
    time.sleep(4)
    print(data)
    logging.info('finalizando job')
    return True