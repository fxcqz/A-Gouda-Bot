import urllib2
import random

apiURL = "http://numbersapi.com/"
randomURL = apiURL+"random"
errors = ['fuck', 'shit', 'wanker', 'bastard', 'oh bollocks', 'shitting hell', 'cunting internet']


def request(num):
    return urllib2.urlopen(str(apiURL+str(num))).read()

def requestDate(month, day):
    return urllib2.urlopen(str(apiURL+str(month) + "/" + str(day) + "/date")).read()

def getFact(data):
    if(len(data) == 4):
        return requestDate(data[3], data[2])
    if(len(data) == 3):
        return request(data[2])
    else:
        return urllib2.urlopen(randomURL).read()

def main(irc, nick, data, handler):
    if len(data) <= 4:
        try:
            if data[0] == "Gouda:" and data[1] == "nf":
                irc.message(getFact(data))
            else:
                irc.message(random.choice(errors))
        except IndexError:
            irc.message(random.choice(errors))
    else:
        irc.message(random.choice(errors))