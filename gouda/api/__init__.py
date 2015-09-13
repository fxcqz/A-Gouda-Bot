import web


class Api(object):
    def __init__(self, irc=None, loader=None, settings=None):
        self.irc = irc
        self.loader = loader
        self.settings = settings
        self.web = web.Web()

    def message(self, text):
        self.irc.message(text)
