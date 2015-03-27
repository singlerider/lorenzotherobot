import socket
import threading

class TwitchIrc:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('',0))
        self.sock.listen(1)
        self.lines = []
        self.client = None
        self.running = False
        self.cv = threading.Condition()
        threading.Thread(target=self.run).start()

    def getPort(self):
        return self.sock.getsockname()[1]

    def run(self):
        """Main loop. This is automatically started at construction time.
        To end the server call stop()
        """
        self.running = True
        self.client,_ = self.sock.accept()
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
            line, buff = buff.split("\r\n",1)

            self.cv.acquire()
            self.lines.append(line)
            self.cv.notify()
            self.cv.release()

    def stop(self):
        self.running = False
        self.client.close()
        self.sock.close()

    def getOutput(self, timeout = 1):
        self.cv.acquire()
        if not self.lines:
          self.cv.wait(timeout)
        assert self.lines, "Failed to get output after " + str(timeout) +" seconds."
        val = self.lines.pop(0)
        self.cv.release()
        return val

    def simulateMessage(self, user, chan, line):
        #>> :singlerider!singlerider@singlerider.tmi.twitch.tv PRIVMSG #theepicsnail_ :!pokemon me
        self.client.send(":{user}!{user}@{user}.tmi.twitch.tv PRIVMSG {chan} :{line}\r\n".format(
            user=user, chan=chan, line=line))



