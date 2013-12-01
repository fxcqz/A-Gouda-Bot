import os, sys
sys.path.append(os.path.abspath('lib/'))
sys.path.append(os.path.abspath('lib/modules'))
import socket
import urllib2
import re
import importlib
from init import ConfLoad
from net import NetLoad
from mods import ModLoad

class CBot():
    def __init__(self):
        self.confpath = "conf/"
        self.libpath = "lib/"
        self.conf = ConfLoad(self.confpath+"settings.ini")
        self.nick = self.conf.get_nick()
        self.network = self.conf.get_netw()
        self.port = int(self.conf.get_port())
        self.chan = '#'+self.conf.get_chan()
        nl = NetLoad(self.network, self.port, self.nick, self.chan)
        self.irc = nl.conn()
        self.ml = ModLoad()
        self.ml.mod_load("cheese")

    def farg(self, arg):
        """ commands """
        c = arg[4]
        if c == 'omg':
            self.irc.send('PRIVMSG ' + self.chan + ' :\x1b[5mOMG NO WAY!\r\n')
        if c == 'cotd':
            output = self.ml.get_arg('cotd')
            self.irc.send('PRIVMSG ' + self.chan + ' :' + output + '\r\n')

    def getc(self):
        """ for cheese module """
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
