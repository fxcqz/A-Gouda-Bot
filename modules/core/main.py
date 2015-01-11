import random
import time
from threading import Thread

def ayy_lmao(irc):
    time.sleep(5)
    irc.message("...")
    time.sleep(3)
    irc.message("ayy lmao")

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

    if any("like" in w for w in data):
        if random.randint(0, 9) == 5:
            irc.message("1 like = 1 prayer x")

    if any("ayy" in w for w in data) and any("lmao" in w for w in data):
        if random.randint(0, 2) == 1:
            ayy = Thread(target=ayy_lmao, args=(irc,))
            ayy.start()
