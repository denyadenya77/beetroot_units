import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('my_logging.log')
file_handler.setFormatter(formatter)

cs = logging.StreamHandler()
cs.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(cs)

logger.debug('File is running!')
