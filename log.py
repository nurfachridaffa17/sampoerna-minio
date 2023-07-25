import logging
import sys

class Logger:
    def __init__ (self, log_level = logging.INFO):
        logging.basicConfig(
            stream=sys.stdout,
            level=log_level,
            format='%(asctime)s %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S',
        )

    def info(self, msg):
        logging.info(msg)
    
    def warning(self, msg):
        logging.warning(msg)
    
    def error(self, msg):
        logging.error(msg)