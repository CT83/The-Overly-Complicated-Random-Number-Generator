import logging
import os
from logging.handlers import RotatingFileHandler

from shared.utils import create_dir_if_not_exists


class LogManager:

    def init_app(self, app):
        # Configuring Logging
        create_dir_if_not_exists('logs')
        logHandler = RotatingFileHandler(os.path.join('logs', 'info.log'),
                                         maxBytes=100000000, backupCount=5)
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        logHandler.setFormatter(formatter)
        logHandler.setLevel(logging.DEBUG)
        app.logger.setLevel(logging.DEBUG)
        app.logger.addHandler(logHandler)
        return app
