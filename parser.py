class Parser:
    def __init__(self, irc, handler, path):
        self.irc = irc
        self.path = path
        self.handler = handler

    def run(self, line):
        if isinstance(line[1], list):
            line[1][-1] = line[1][-1].replace("\r\n", "")
            line[1][0] = line[1][0].lstrip(':')
        for key, module in self.handler.importlist.iteritems():
            if line[1] != None:
                data = [word.lstrip() for word in line[1]]
                module.main(self.irc, line[0], data, self.handler)
        if len(self.handler.delayed_imports) > 0:
            for imp in self.handler.delayed_imports:
                self.handler.load_module(imp, delay=False)
                self.handler.delayed_imports.remove(imp)
        du_len = len(self.handler.delayed_unloads)
        if du_len > 0:
            for x in range(len(self.handler.delayed_unloads)):
                um_len = len(self.handler.delayed_unloads)
                self.handler.unload_module(self.handler.delayed_unloads.pop(), delay=False)
                if len(self.handler.delayed_unloads) != um_len:
                    self.irc.message("thats an unload! yea boiiii")
                else:
                    self.irc.message("rarely seen error message, might be about unloading lol")
