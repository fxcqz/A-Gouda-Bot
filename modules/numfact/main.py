import urllib2
import random

apiURL = "http://numbersapi.com/"
randomURL = apiURL+"random"
errors = ['fuck', 'shit', 'wanker', 'bastard', 'oh bollocks', 'shitting hell', 'cunting internet']


def request(num):
    res = None
    try:
        res = urllib2.urlopen(str(apiURL+str(num))).read()
    except urllib2.HTTPError:
        pass
    return res

def requestDate(month, day):
    res = None
    try:
        res = urllib2.urlopen(str(apiURL+str(month) + "/" + str(day) + "/date")).read()
    except urllib2.HTTPError:
        pass
    return res

def getFact(data):
    res = None
    if(len(data) == 4):
        return requestDate(data[3], data[2])
    if(len(data) == 3):
        return request(data[2])
    else:
        try:
            res = urllib2.urlopen(randomURL).read()
        except urllib2.HTTPError:
            pass
    return res

def main(irc, nick, data, handler):
    if len(data) <= 4:
        try:
            if data[0] == "Gouda:" and data[1] == "nf":
                d = getFact(data)
                if d:
                    irc.message(getFact(data))
        except IndexError:
            pass
