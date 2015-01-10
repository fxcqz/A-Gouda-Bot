from config_loader import ConfigLoader
from irc import Irc
from parser import Parser
from module_handler import ModuleHandler

class Gouda:
    def __init__(self):
        self.config_path = "config/"
        self.module_path = "modules/"
        self.configure()
        self.irc = Irc(self.nick, self.channel)
        # load modules here
        self.module_handler = ModuleHandler(self.module_path)
        self.parser = Parser(self.irc, self.module_handler, self.module_path)
        # always load the following:
        self.module_handler.load_module("loader", delay=False)
        self.module_handler.load_module("core", delay=False)

    def configure(self):
        config = ConfigLoader(self.config_path + "settings.ini")
        self.nick = config.get_nick()
        self.network = config.get_network()
        self.port = config.get_port()
        self.channel = config.get_channel()

    def run(self):
        self.irc.connect(self.network, self.port)
        while True:
            data = self.irc.receive()
            self.irc.pong(data)
            self.irc.knock_check(data)
            line = self.irc.read(data)
            # send line to parser
            # parser is where modules are loaded etc
            self.parser.run(line)

if __name__ == '__main__':
    gouda = Gouda()
    gouda.run()
