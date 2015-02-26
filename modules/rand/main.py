import word
import yesno
from threading import Thread

def run(irc):
    msg = word.sentence(["DT", ["JJ", "JJS"], ["NN", "NNS"], ["VB", "VBD"], "RB"], "/usr/share/dict/british-english")
    irc.message(msg)

def main(irc, nick, data, handler):
    reload(word)
    reload(yesno)
    if data[0] == "Gouda:" and len(data) > 2:
        if data[1] == "random":
            if data[2] == "sentence":
                retriever = Thread(target=run, args=(irc,))
                retriever.start()
    yesno.yesno(irc, nick, data, handler)
