import urllib2
from bs4 import BeautifulSoup
import random

def get_page(url):
    data = None
    try:
        response = urllib2.urlopen(url)
        data = response.read()
    except urllib2.HTTPError as err:
        pass
    return data

def get_responses(url):
    data = get_page(url)
    links_list = []
    if data != None:
        soup = BeautifulSoup(data)
        posts = soup.find_all('div', attrs={'class': 'result-link'})
        for tag in posts:
            if tag.a['href'] != None:
                links_list.append(tag.a['href'])
    return links_list

def choose_link(irc, url):
    failure_msg = ["Don't ask me, I'm a cheese based life form...", "What kind of a question is that?", "I actually know this one, but I'm not going to tell you lol", "Huh... you're STILL stuck on that?!"]
    responses = get_responses(url)
    if len(responses) > 0:
        irc.message("http://stackoverflow.com" + responses[random.randint(0, len(responses)-1)])
    else:
        irc.message(failure_msg[random.randint(0, len(failure_msg)-1)])

def main(irc, nick, data, handler):
    length = len(data)
    if length > 3:
        if data[0] == "Gouda:" and data[1] == "so":
            term = '+'.join(data[2:])
            choose_link(irc, "http://stackoverflow.com/search?q=" + term)
