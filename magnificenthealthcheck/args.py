import argparse
import logging

try:
    from UserDict import UserDict
except ImportError: # pragma nocover
    from collections import UserDict

class Arguments(UserDict, object):
    def __init__(self, args=None):
        self.log = logging.getLogger(__name__)
        self.data = self._parse_arguments(args)
        self.log.debug("Parsed arguments: %s", self.data)

    def _parse_arguments(self, args=None):
        """Parse arguments.

        :type args: list
        :param args: Command line arguments.

        :rtype: dict
        :return: Parsed arguments.
        """
        parser = argparse.ArgumentParser()

        parser.add_argument('url', help='URL to check')

        parser.add_argument('-i',
                            '--interval',
                            default=5,
                            help='Interval of checking URL. Default: 5')

        parser.add_argument('-r',
                            '--rise',
                            default=2,
                            help='Tests pass before rise. Default: 2')

        parser.add_argument('-f',
                            '--fail',
                            default=3,
                            help='Tests failed before fail. Default: 3')

        parser.add_argument('--daemon',
                            default=False,
                            action='store_true',
                            help='Run process as a daemon. Default: False')

        parser.add_argument('-D',
                            '--debug',
                            default=False,
                            action='store_true',
                            help='Change verbosity level to DEBUG. Default: False')

        result = parser.parse_args(args)

        return vars(result)
