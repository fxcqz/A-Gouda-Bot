import socket
import urllib2
import re

class CBot():
    def __init__(self):
        self.nick = 'cbot_dot_py'
        self.debug = False
        self.network = "irc.aberwiki.org"
        self.port = 6667
        self.chan = '#flash'
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.network,self.port))
        self.irc.recv(4096)
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER CheeseBot CheeseBot CheeseBot :Cheese IRC\r\n')
        self.irc.send('JOIN ' + self.chan + '\r\n')
        self.irc.send('PRIVMSG ' + self.chan + ' :Lol.\r\n')

    def farg(self, arg):
        c = arg[4]
        if c == 'omg':
            self.irc.send('PRIVMSG ' + self.chan + ' :OMG NO WAY!\r\n')
        if c == 'cheese':
            self.getc()

    def getc(self):
        response = urllib2.urlopen('http://cheese.com')
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
                if func == 'cbot_dot_py:':
                    arg = data.split()
                    self.farg(arg)

if __name__ == '__main__':
    bot = CBot()
    bot.run()
