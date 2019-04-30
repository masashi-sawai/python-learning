import logging


def do_something():
    # outputLogging を入れてみる
    logger = logging.getLogger('outputLogging')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
