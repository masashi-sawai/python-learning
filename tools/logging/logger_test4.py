import logging.config

import logger_load

# main 処理なので、__name__ には、root が入る
logging.config.fileConfig('./logging.ini')
logger = logging.getLogger('__name__')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

logger_load.do_something()
