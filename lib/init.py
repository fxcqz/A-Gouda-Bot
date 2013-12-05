import ConfigParser
import json

class ConfLoad:
    def __init__(self, f):
        conf = ConfigParser.ConfigParser()
        conf.read(f)
        self.nick = conf.get("Core", "nick")
        self.admins = json.loads(conf.get("Core", "admins"))
        for x in range(len(self.admins)):
            self.admins[x] = str(self.admins[x])
        if conf.get("Core", "chan")[:1] == '#':
            self.chan = conf.get("Core", "chan")
        else:
            self.chan = '#'+conf.get("Core", "chan")
        self.port = int(conf.get("Network", "port"))
        self.network = conf.get("Network", "server")

    def get_nick(self):
        return self.nick

    def get_chan(self):
        return self.chan

    def get_port(self):
        return self.port

    def get_netw(self):
        return self.network

    def get_admins(self):
        return self.admins
