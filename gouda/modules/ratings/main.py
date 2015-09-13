import random


def main(message, api):
    if message[0] == "rate":
        api.message("%d/8" % random.randint(0, 8))
    elif message[0][0] == 'r' and message[0][1].isdigit():
        try:
            dot = message[0].find('.')
            type_ = float if dot != -1 else int
            base = type_(message[0][1:])
            rating = random.uniform(0., base) if dot != -1 else random.randint(0, base)
            api.message("{0}/{1}".format(rating, base))
        except ValueError:
            api.message("%d/8" % random.randint(0, 8))
