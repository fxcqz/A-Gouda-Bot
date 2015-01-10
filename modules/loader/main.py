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
            handler.load_module(tokens[2])
            irc.message("Loaded module: " + tokens[2])
        else:
            irc.message(tokens[2] + " already exists, dummy")

def modreload(irc, handler, tokens):
    if tokens[1] == "reload":
        if handler.importlist[tokens[2]] != None:
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
