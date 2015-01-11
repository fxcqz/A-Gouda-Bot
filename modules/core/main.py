def get_modules(handler):
    ret = "No modules loaded"
    if handler.importlist:
        modules = [key for key in handler.importlist]
        ret = ', '.join(modules)
    return ret

def main(irc, nick, data, handler):
    if data[0][:-1] == "Gouda" and len(data) > 1:
        # message is addressed to the bot
        if data[1] == "commands":
            irc.message("You can't command me, I'm a free spirit!")

        if data[1] == "modules":
            irc.message("Modules currently loaded are: " + get_modules(handler))
