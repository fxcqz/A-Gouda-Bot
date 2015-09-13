from threading import Thread
import time

from .loader import Loader


class Parser(object):
    def __init__(self, api, irc, settings):
        self.api = api
        self.cache = {"mains": {}}
        self.irc = irc
        self.loader = Loader(api, settings)
        self.settings = settings
        self.api.loader = self.loader
        self.api.settings = self.settings

    def _parse(self, message, explicit):
        for module in self.loader.importlist:
            try:
                meta = self.loader.importlist[module].META
                if "justmain" in meta:
                    # just run the main function
                    meta['justmain'](message, self.api)
                    # consider some matching function which determines when
                    # to attempt main func cache call
                    self.cache['mains'][module] = meta['justmain']
                else:
                    try:
                        # check for commands
                        commands = meta['commands']
                        for command in commands:
                            if message[0] == command:
                                # run the command, perhaps parse arg requirements
                                # here first and then call with args
                                if 'explicit' in commands[command]:
                                    if commands[command]['explicit'] is True:
                                        # only call explicit functions if they are addressed to the bot
                                        if explicit:
                                            commands[command]['function'](message, self.api)
                                else:
                                    commands[command]['function'](message, self.api)
                                self.cache[command] = commands[command]['function']

                        # check for context
                        context = meta['context']
                        if context['function'] is not None:
                            if context['function'](''.join(message)) is True:
                                # if it makes sense to run the function
                                context['result'](message, self.api)
                    except KeyError:
                        # no context, no big deal
                        pass
            except AttributeError as ae:
                # potentially still search for a main function
                try:
                    mainfile = self.loader.importlist[module].mainfile
                    mainmod = self.loader.load_module("gouda.modules.%s.%s" % (module, mainfile))
                    if hasattr(mainmod, "main"):
                        self.loader.importlist[module].META['context']['function'] = lambda x: True
                        self.loader.importlist[module].META['context']['result'] = mainmod.main
                        mainmod.main(message, self.api)
                except AttributeError:
                    # someone really didnt want their function to run
                    pass
                print module, ae

    def extract_message(self, message, cmd=False):
        explicit = False
        offset = 0
        if message[0][:-1] == self.settings.core['nick']:
            explicit = True
            offset = 1
        message = message[offset:]
        if cmd and len(message) > 1:
            message = message[1:]
        return message, explicit

    def cache_call(self, message):
        if message[0] in self.cache:
            self.cache[message[0]](message, self.api)
            return True
        return False

    def parse(self, (nick, message, info)):
        """
        Parses lines read from irc and sends them to the appropriate modules
        """
        message, explicit = self.extract_message(message)
        if len(message) > 0:
            if not self.cache_call(message):
                self._parse(message, explicit)
        self.loader.do_imports()
        self.loader.do_unloads()

    def __call__(self, data):
        if data[1] is not None:
            self.parse(data)
