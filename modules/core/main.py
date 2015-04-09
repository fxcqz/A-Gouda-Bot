import random
import time
import nltk
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

def adj_rudeness(data, irc):
    tags = nltk.pos_tag(data)
    adjs = []
    for t in tags:
        if t[1] == "JJ":
            adjs.append(t[0])
    if len(adjs) > 0:
        a = ["cunt", "bitch", "friend", "ally", "comrade", "nob", "dick", "twat", "m8"]
        b = ["mum", "dad", "nan", "sister"]
        irc.message("I tell you what else is "+random.choice(adjs)+", "+random.choice(a)+". Your "+ random.choice(b) +".")

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
        if random.randint(0, 8) == 1:
            ayy = Thread(target=ayy_lmao, args=(irc,))
            ayy.start()

    if data[0] == "lol":
        if random.randint(0, 20) == 4:
            irc.message("lol")

    if len(data) > 1 and random.randint(0,50) == 11:
        adj_rudeness(data, irc)
