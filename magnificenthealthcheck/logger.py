import logging
import os
import sys


class Logger(logging.getLoggerClass()):
    """Logger class for muliple thread logging.

    It writes debug messages to the file.

    :rtype: :class:`logging.RootLogger`
    :return: Configured logger object.
    """

    def __init__(self, name=None, log_level=None, log_dir=None):

        self.date_format = '%H:%M:%S'
        self.log_level = log_level
        self.name = name

        self.file_log_format = '%(asctime)s %(levelname)s %(filename)s' \
                               '[%(lineno)d] %(funcName)s: ' \
                               '%(message)s'

        self.log_name = self.name
        default_log_dir = os.path.join(self.get_log_dir(), self.name)
        self.log_dir = log_dir if log_dir else default_log_dir
        self.log_file = os.path.join(self.log_dir, self.log_name)

        # Configure the logger
        self.configure()

    def __get__(self):
        return self

    def configure(self):
        """Configure the logger object."""

        # Use specified log_dir or the default one
        self.create_dir(self.log_dir)

        # Create handlers
        file_handler = logging.FileHandler(self.log_file, mode='a')

        # Create formatters
        file_log_format = logging.Formatter(fmt=self.file_log_format,
                                            datefmt=self.date_format)

        # Attach formatters
        file_handler.setFormatter(file_log_format)

        # Create logger
        logging.Logger.__init__(self, self.log_name, level=self.log_level)

        # Configure logging level
        self.setLevel(self.log_level)
        file_handler.setLevel(self.log_level)

        # Attach handlers
        self.addHandler(file_handler)
        logging.getLogger('').addHandler(file_handler)

    def get_log_dir(self):
        """Return logging directory based on syetem platform.

        Default: /var/log

        :rtype: str
        :return: Path to log directory
        """

        log_dir = {'darwin': '~/Library/Logs'}
        result = log_dir.get(sys.platform, '/var/log')
        return os.path.expanduser(result)

    def create_dir(self, name):
        """Recursively creates directores if it doesn't exist

        :type: str
        :param: The directory three path
        """

        if not os.path.exists(name):
            os.makedirs(name)
