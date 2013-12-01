import ConfigParser

class ConfLoad:
    def __init__(self, f):
        conf = ConfigParser.ConfigParser()
        conf.read(f)
        self.nick = conf.get("Core", "nick")
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
