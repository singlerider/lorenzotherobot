import socket
import threading

import globals

MOD_USER = "singlerider"
REG_USER = "randomuser"
TEST_CHANNEL = "#theepicsnail_"
TEST_CHAN = TEST_CHANNEL.lstrip("#")
ALT_USER = "curvyllama"  # should be an actual streamer
USERS = {
    "chatters": {
        "moderators": [TEST_CHAN, MOD_USER],
        "global_mods": [],
        "admins": [],
        "viewers": [REG_USER],
        "staff": []
         },
    "_links": {},
    "chatter_count": 3
}
globals.CHANNEL_INFO[TEST_CHAN] = {
    "caught": True, "pokemon": "", "viewers": USERS
}


class TwitchIrc:

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(("", 0))
        self.sock.listen(1)
        self.lines = []
        self.client = None
        self.running = False
        self.cv = threading.Condition()
        threading.Thread(target=self.run).start()

    def get_port(self):
        return self.sock.getsockname()[1]

    def run(self):
        """Main loop. This is automatically started at construction time.
        To end the server call stop()
        """
        self.running = True
        self.client, _ = self.sock.accept()
        self.client.settimeout(.1)
        self.client.send(":tmi.twitch.tv 001 testUsername :Welcome, GLHF!\r\n")
        self.client.send(":tmi.twitch.tv 376 testUsername :>\r\n")
        buff = ""
        while self.running:
            if "\r\n" not in buff:
                try:
                    data = self.client.recv(1024)
                    buff += data
                except:
                    continue
            line, buff = buff.split("\r\n", 1)
            self.cv.acquire()
            self.lines.append(line)
            self.cv.notify()
            self.cv.release()

    def stop(self):
        self.running = False
        self.client.close()
        self.sock.close()

    def get_output(self, timeout=1):
        self.cv.acquire()
        if not self.lines:
            self.cv.wait(timeout)
        assert self.lines, "Failed to get output after " + \
            str(timeout) + " seconds."
        print self.lines[0]
        val = self.lines.pop(0)
        self.cv.release()
        return val

    def simulate_message(self, user, chan, line):
        self.client.send(
            ":{user}!{user}@{user}.tmi.twitch.tv PRIVMSG {chan} \
:{line}\r\n".format(user=user, chan=chan, line=line))
