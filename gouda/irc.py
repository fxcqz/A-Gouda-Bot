import socket
import time


class Irc(object):
    def __init__(self, (nick, channel, names)):
        self.connection = None
        self.channel = channel
        self.nick = nick
        self.knocking = False
        self.names = names

    def connect(self, (net, port)):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((net, port))
        self.connection.recv(4096)
        self.connection.send('NICK %s\r\n' % self.nick)
        self.connection.send('USER %s %s %s :%s\r\n' % self.names)

    def join(self):
        self.connection.send('JOIN %s\r\n' % self.channel)

    def pong(self, data):
        if data.find('PING') != -1:
            self.connection.send('PONG %s\r\n' % data.split()[1])

    def quit(self, msg):
        self.connection.send('QUIT :%s\r\n' % msg)

    def message(self, text):
        self.connection.send('PRIVMSG %s :%s\r\n' % (self.channel, text))

    def _knock(self):
        self.connection.send('KNOCK %s\r\n' % self.channel)

    def knock(self, data):
        if data[-6:-2] == '(+i)' and self.knocking is False:
            self._knock()
            self.knocking = True
        if 'INVITE' in data:
            self.join()

    def read(self, data):
        user, message, info = None, None, None
        if data.find('PRIVMSG') != -1:
            user = data.split('!')[0].replace(':', '')
            message = data.split()[3:]
            message[0] = message[0][1:]
            info = data.split()
        return user, message, info

    def receive(self):
        return self.connection.recv(4096)
