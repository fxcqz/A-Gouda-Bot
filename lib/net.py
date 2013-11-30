import socket

class NetLoad:
    def __init__(self, net, port, nick, chan):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((net, port))
        self.irc.recv(4096)
        self.irc.send('NICK ' + nick + '\r\n')
        self.irc.send('USER GoudaBot GoudaBot GoudaBot :Gouda IRC\r\n')
        self.irc.send('JOIN ' + chan + '\r\n')

    def conn(self):
        return self.irc
