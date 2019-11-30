# Make a program that can write stuff using the logging module.

import logging

logging.basicConfig(filename='make_logging_task.log', level=logging.DEBUG)

logging.debug('logging debug')
logging.info('logging info')
logging.warning('logging warning')
logging.error('logging error')
logging.critical('logging critical')
