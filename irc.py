import socket
import time

class Irc:
    def __init__(self, nick, channel):
        self.irc = None
        self.channel = channel
        self.nick = nick
        self.knocking = False

    def connect(self, net, port):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((net, port))
        self.irc.recv(4096)
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER GoudaBot GoudaBot GoudaBot :Gouda IRC\r\n')

    def join(self):
        self.irc.send('JOIN ' + self.channel + '\r\n')

    def pong(self, data):
        if data.find('PING') != -1:
            self.irc.send('PONG ' + data.split()[1] + '\r\n')

    def quit(self, text):
        self.irc.send('QUIT :' + text + '\r\n')

    def message(self, text):
        try:
            self.irc.send('PRIVMSG ' + self.channel + ' :' + text + '\r\n')
        except UnicodeEncodeError:
            pass

    def emote(self, text):
        self.irc.send('\001ACTION ' + text + '\001')

    def knock(self):
        self.irc.send('KNOCK ' + self.channel + '\r\n')

    def knock_check(self, data):
        if data[-6:-2] == "(+i)" and self.knocking == False:
            self.knock()
            self.knocking = True
        if 'INVITE' in data:
            self.join()

    def read(self, data):
        user, message, info = None, None, None
        print data
        if data.find('PRIVMSG') != -1:
            user = data.split('!')[0].replace(':', '')
            message = data.split()[3:]
            info = data.split()
        return [user, message, info]

    def receive(self):
        return self.irc.recv(4096)
