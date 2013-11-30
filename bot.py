import os, sys
sys.path.append(os.path.abspath('lib/'))
import socket
import urllib2
import re
from init import ConfLoad

class CBot():
    def __init__(self):
        """ setup """
        self.confpath = "conf/"
        self.libpath = "lib/"
        self.conf = ConfLoad(self.confpath+"settings.ini")
        self.nick = self.conf.get_nick()
        self.debug = False
        self.network = self.conf.get_netw()
        self.port = int(self.conf.get_port())
        self.chan = '#'+self.conf.get_chan()
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.network,self.port))
        self.irc.recv(4096)
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER CheeseBot CheeseBot CheeseBot :Cheese IRC\r\n')
        self.irc.send('JOIN ' + self.chan + '\r\n')

    def farg(self, arg):
        c = arg[4]
        if c == 'omg':
            self.irc.send('PRIVMSG ' + self.chan + ' :OMG NO WAY!\r\n')
        if c == 'cheese':
            self.getc()

    def getc(self):
        response = urllib2.urlopen('http://cheese.com')
        if response:
            m = re.search( r'style="color:.*">(.*)</a></h4>', response.read(), re.M|re.I)
            if m:
                self.irc.send('PRIVMSG ' + self.chan + ' : The cheese of the day is: ' + m.group(1)+'\r\n')

    def run(self):
        while True:
            data = self.irc.recv(4096)
            if data.find('PING') != -1:
                self.irc.send('PONG ' + data.split()[1] + '\r\n')
            elif data.find('PRIVMSG') != -1:
                message = ':'.join(data.split(':')[2:])
                ni = data.split('!')[0].replace(':', ' ')
                dest = ''.join(data.split(':')[:2]).split(' ')[-2]
                func = message.split()[0]
                if func == self.nick+':':
                    arg = data.split()
                    self.farg(arg)

if __name__ == '__main__':
    bot = CBot()
    bot.run()
