import random
import re
import nltk
import string


modals = ["can", "could", "may", "might", "shall", "should", "will", "would", "must", "ought", "are", "am", "is", "does", "did", "didnt", "didn't", "do", "don't"]

def yn(irc):
    yes = ["yes", "m8.... yes!!", "yea duh", "i will be boring and say yes", "yup", "aye"]
    no = ["no", "nononononono", "nahh", "fuck that", "nope", "NO!", "yes... just kidding, no.", "no way!!", "seriously? no, man..."]
    irc.message(random.choice([random.choice(yes), random.choice(no)]))
    #irc.message(random.choice(yes))

def phrase(data):
    text = nltk.word_tokenize(' '.join(data))
    ts = []
    try:
        ts = nltk.pos_tag(text)
    except UnicodeDecodeError:
        pass
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
        if data[0] != "Gouda:" and data[0][-1] == ":":
            pass
        elif len(data) == 2:
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

def rand_adv():
    adv = ""
    with open("/usr/share/dict/british-english", 'r') as f:
        words = f.readlines()
        words = [w.strip('\n') for w in words]
        while adv[-2:] != "ly" and nltk.pos_tag([adv])[0][1] not in ["RB"]:
            adv = random.choice(words)
    return adv

def yesno(irc, nick, data, handler):
    offset = 0
    if data[0] == "Gouda:":
        if len(data) > 1:
            offset = 1
    if data[offset] == 'yn':
        yn(irc)
    if data[offset] in modals and data[-1][-1] == "?":
        yn(irc)
    or_(data[offset:], irc)
    if data[offset] == "when" and len(data[offset:]) > 1:
        if data[offset+1] in modals and data[-1][-1] == "?":
            hrs = random.randint(0, 23)
            mins = random.randint(0, 59)
            shrs = str(hrs)
            smins = str(mins)
            if hrs < 10:
                shrs = "0" + shrs
            if mins < 10:
                smins = "0" + smins
            irc.message(shrs + ":" + smins)
    if data[offset] == "why" and len(data[offset:]) > 1:
        if data[offset+1] in modals and data[-1][-1] == "?":
            whys = ["because i said so", "why not?", "itll make you feel better about your worthless life", "i would"]
            irc.message(random.choice(whys))
    if data[offset] == "how" and len(data[offset:]) > 1:
        if data[offset+1] in modals and data[-1][-1] == "?":
            radv = rand_adv()
            if radv != "":
                irc.message(radv)
            else:
                irc.message("shit, i don't know, man")
    if "lisp" in data[offset:]:
        irc.message(random.choice(["lisp, lisp, lisp.. always with the lisp!", "are you on about fucking lisp again...", "check out my lithp", "hi im a hipster that wishes it was still 1960"]))
    elif data[-1] == "lo":
        irc.message("l")
    elif data[-1] == "yh?":
        irc.message(random.choice(["yea", "yup", "yes you fuckwit"]))
    elif data[-1] == "kik]":
        irc.message("lel")
    elif data[offset] == "roulette":
        rcol = random.choice([" red", " black"])
        irc.message(str(random.choice(range((2 - (ord(rcol[2]) % 2)), 37, 2)))+str(rcol))
    elif data[offset] == "acronym":
        ac_ret = ""
        ac_num = 3
        if len(data) > 2:
            try:
                ac_num = int(data[2])
            except ValueError:
                pass
        ac_src = string.letters[:26]
        ac_src.replace('x', random.choice('aeiou'))
        for x in range(ac_num):
            ac_ret += random.choice(ac_src)
        irc.message(ac_ret)
    elif data[-1] == "bk":
        irc.message("wb")
    if "can't" in data[offset:]:
        cb_s = ' '.join(data[offset:])
        cb_c = cb_s.find("can't")
        cb_b = cb_s.find("believe")
        if cb_b != -1 and cb_b > cb_c:
            irc.message("I can't believe it's not butter")
