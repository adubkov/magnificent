import logging
import os
import time
import sys

import requests
import retry

from .args import Arguments
from .logger import Logger

class MagnificentHealthcheck(object):
    def __init__(self):
        args = Arguments()
        self._run(args)

    def _run(self, args):
        #import pdb; pdb.set_trace()

        log_level = logging.DEBUG if args['debug'] else logging.INFO
        self.log = Logger(name=self.__class__.__name__, log_level=log_level)

        self.log.debug("Arguments: %s", args)

        if args['daemon']:
            self._daemon()

        self.log.info('Start Magnificent healthcheck!')
        self._checking_loop(args)

    def _daemon(self):
        pid = os.fork()
        if pid == 0:
            os.setsid()
        else:
            sys.exit(0)
        return pid

    def _checking_loop(self, args):
        url = args['url']
        interval = int(args['interval'])
        r = int(args['rise'])
        f = int(args['fail'])
        history_len = r + f

        history = []

        while True:
            res = requests.get(url)
            status = res.status_code

            history.append(status == 200)

            if len(history) > history_len:
                history.pop(0)

            self.log.debug("History: %s", history)
            # checking for rise or fail
            if all(history[-r:]) and len(history) >= history_len:
                self.log.info("Magnificent feels good now :)")
            elif not any(history[-f:]) and len(history) >= history_len:
                self.log.info("Magnificent feels bad :'(")

            self.log.debug("%s %s", url, status)

            time.sleep(interval)

def run():
    MagnificentHealthcheck()

if __name__ == '__main__':
    run()
