import ConfigParser
import json

class ConfigLoader:
    def __init__(self, config_file):
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        self.nick = config.get("Core", "nick")
        if config.get("Core", "channel")[:1] == '#':
            self.channel = config.get("Core", "channel")
        else:
            self.channel = '#'+config.get("Core", "channel")
        self.port = int(config.get("Network", "port"))
        self.network = config.get("Network", "server")

    def get_nick(self):
        return self.nick

    def get_channel(self):
        return self.channel

    def get_port(self):
        return self.port

    def get_network(self):
        return self.network
