import urllib2
from bs4 import BeautifulSoup
import datetime

class Cheese:
    def __init__(self, irc):
        self.day = self.get_day()
        self.data = None
        self.cotd = None
        self.output = None
        self.irc = irc

    def get_day(self):
        return datetime.datetime.now().strftime("%A")

    def get_page_contents(self, page):
        try:
            response = urllib2.urlopen(page)
            self.data = response.read()
        except urllib2.HTTPError as err:
            self.output = "Could not open " + page

    def get_cotd(self):
        self.get_page_contents("http://www.cheese.com/")
        try:
            soup = BeautifulSoup(self.data)
            cotd_div = soup.find('div', attrs={'class': 'top-offer'})
            self.cotd = cotd_div.a.get('href').replace('/', '')
        except AttributeError:
            self.output = "Could not find the cheese of the day"

    def set_output(self):
        if self.cotd != None:
            self.output = "The cheese of the day is: " + self.cotd
        elif self.cotd == None and self.output == None:
            self.output = "Unable to retrieve the cheese of the day"

    def run(self):
        if self.cotd == None or self.day != self.get_day():
            self.get_cotd()
        self.set_output()
        self.irc.message(self.output)

def main(irc, nick, data, handler):
    if len(data) == 2:
        if data[0] == "Gouda:" and data[1] == "cotd":
            cheese = Cheese(irc)
            cheese.run()
