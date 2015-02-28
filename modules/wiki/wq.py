import urllib2
import re
import string
import random
import simplejson
from bs4 import BeautifulSoup

def gquery(query):
    try:
        inforeq = urllib2.Request("http://en.wikipedia.org/wiki/"+query.replace(" ", "_"), None, {'Referer': "gbot"})
        infores = urllib2.urlopen(inforeq)

        soup = BeautifulSoup(infores)
        sentences = []
        for text in soup.find_all("p"):
            for sentence in text.text.lstrip().rstrip().split("."):
                sentences.append(sentence)
        if len(sentences) > 0:
            rets = ""
            rets = random.choice(sentences)
            while not all(c in string.printable for c in rets) and len(rets) == 0:
                rets = random.choice(sentences)
            return re.sub("\[[0-9]+\]", "", rets).lstrip().rstrip()
    except urllib2.HTTPError:
        return ""
    return ""

def query(irc, nick, data, handler):
    offset = 0
    if data[0] == "Gouda:":
        offset = 1
    if data[offset] == "wiki" and len(data) > 1:
        res = gquery(' '.join(data[offset+1:]))
        if res != "":
            irc.message(res)
        else:
            irc.message("no data found m8")
