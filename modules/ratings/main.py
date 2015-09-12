import random


def main(irc, nick, data, handler):
    offset = 0
    if data[0] == "Gouda:":
        offset = 1
    if len(data) >= 3:
        if data[offset] == "rate":
            rating = random.randint(0, 8)
            irc.message(str(rating)+"/8")
        elif len(data[offset]) > 1:
            if data[offset][1].isdigit() and data[offset][0] == 'r':
                try:
                    dot = data[offset].find('.')
                    t_ = float if dot != -1 else int
                    base = t_(data[offset][1:])
                    rating = random.uniform(0.0, base) if dot != -1 else random.randint(0, base)
                    irc.message(str(rating)+"/"+str(base))
                except ValueError:
                    rating = random.randint(0, 8)
                    irc.message(str(rating)+"/8")
