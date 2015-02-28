import wq


def main(irc, nick, data, handler):
    reload(wq)
    wq.query(irc, nick, data, handler)
