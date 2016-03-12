import time
from threading import Thread


def initialize(IRC, crons):
    # start up the cron jobs.
    # config should be in the structure of
    # {
    #   "#channel": [ (period, enabled, callback),.... ]
    #   ...
    # }
    for channel, jobs in crons.items():
        # jobs can be [], False, None...
        if not jobs:
            continue

        for (delay, enabled, callback) in jobs:
            if not enabled:
                continue

            CronJob(IRC, channel, delay, callback).start()


class CronJob(Thread):

    def __init__(self, IRC, channel, delay, callback):
        Thread.__init__(self)
        self.daemon = True
        self.delay = delay
        self.callback = callback
        self.IRC = IRC
        self.channel = channel

    def run(self):
        while True:
            time.sleep(self.delay)
            resp = self.callback(self.channel)
            self.IRC.send_message(self.channel, resp)
            self.IRC.send_alt_message(self.channel, resp)
