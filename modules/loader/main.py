from os import listdir
from os.path import isdir, join


def check(tokens):
    status = False
    if len(tokens) > 2:
        if tokens[0] == "Gouda:" and tokens[2] != 'loader':
            status = True
    return status

def modload(irc, handler, tokens):
    if tokens[1] == "load":
        exists = False
        for key in handler.importlist:
            if key == tokens[2]:
                exists = True
        if exists == False:
            if tokens[2] == "all":
                for m in [f for f in listdir("modules/") if isdir(join("modules/", f))]:
                    if m != "loader":
                        handler.load_module(m)
            else:
                handler.load_module(tokens[2])

def modreload(irc, handler, tokens):
    if tokens[1] == "reload":
        if tokens[2] in handler.importlist:
            reload(handler.importlist[tokens[2]])
            irc.message("Reloaded module: " + tokens[2])
        else:
            irc.message("Failed to reload module: " + tokens[2] + ", module is not loaded.")

def modunload(irc, handler, tokens):
    if tokens[1] == "unload":
        for key in handler.importlist:
            if key == tokens[2]:
                handler.unload_module(tokens[2])

def main(irc, nick, data, handler):
    if check(data):
        modload(irc, handler, data)
        modreload(irc, handler, data)
        modunload(irc, handler, data)
