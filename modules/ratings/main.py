import random


def main(irc, nick, data, handler):
    offset = 0
    if data[0] == "Gouda:":
        offset = 1
    if len(data) >= 3:
        if data[offset] == "rate" or data[offset] == "r8":
            rating = random.randint(0, 10)
            irc.message(str(rating)+"/10")
