"""
Cheese bot of love. xo
"""
from .irc import Irc
from .parser import Parser
from .settings import Settings
from .utils import Join
from api import Api


class Gouda(object):
    def __init__(self):
        self.settings = Settings("config/settings.json")
        self.irc = Irc(self.settings.ircinit)
        self.api = Api(irc=self.irc)
        self.parser = Parser(self.api, self.irc, self.settings)

    @Join
    def run(self):
        while True:
            data = self.irc.receive()
            self.irc.pong(data)
            self.irc.knock(data)
            self.parser(self.irc.read(data))
