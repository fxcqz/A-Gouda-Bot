import random
import nltk


modals = ["can", "could", "may", "might", "shall", "should", "will", "would", "must", "ought"]

def yn(irc):
    yes = ["yes", "m8.... yes!!", "yea duh", "i will be boring and say yes", "yup", "aye", "do it you sack of shit!"]
    no = ["no", "nononononono", "nahh", "fuck that", "nope", "NO!", "yes... just kidding, no.", "no way!!", "seriously? no, man..."]
    irc.message(random.choice([random.choice(yes), random.choice(no)]))

def phrase(data):
    text = nltk.word_tokenize(' '.join(data))
    ts = nltk.pos_tag(text)
    phrase = []
    for n in ts:
        if n[1] in ["JJ", "JJS", "JJR"]:
            phrase.append(n[0])
        if n[1] in ["NN", "NNS", "NNP"]:
            phrase.append(n[0])
            break
    return ' '.join(phrase)

def or_(data, irc):
    if "or" in data:
        if len(data) == 2:
            pass
        elif len(data) > data.index("or")+1 and data[-1][-1] == "?":
            p1 = phrase(data)
            p2 = phrase(data[data.index("or")+1:])
            if len(p1) > 0 and len(p2) > 0:
                response = random.choice([p1, p2])
                if response[-1] == "?":
                    response = response[:-1]
                irc.message(random.choice([p1, p2]))
            elif len(p1) > 0 and len(p2) == 0:
                irc.message(random.choice([p1, ' '.join(data[data.index("or")+1:])]).strip("?"))
            elif len(p2) > 0 and len(p1) == 0:
                irc.message(random.choice([p2, ' '.join(data[:data.index("or")])]).strip("?"))
            else:
                pass

def yesno(irc, nick, data, handler):
    offset = 0
    if data[0] == "Gouda:":
        if len(data) > 1:
            offset = 1
    if "yn" in data[offset]:
        yn(irc)
    if data[offset] in modals and data[-1][-1] == "?":
        yn(irc)
    or_(data[offset:], irc)
