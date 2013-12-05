import os, sys
import socket
import importlib

sys.path.append(os.path.abspath('lib/'))
sys.path.append(os.path.abspath('lib/core/'))
sys.path.append(os.path.abspath('lib/modules/'))
from init import ConfLoad
from net import NetLoad
from mods import ModLoad

import loader

class CBot():
    def __init__(self):
        self.confpath = "conf/"
        self.libpath = "lib/"
        self.conf = ConfLoad(self.confpath+"settings.ini")
        self.nick = self.conf.get_nick()
        self.network = self.conf.get_netw()
        self.port = self.conf.get_port()
        self.chan = self.conf.get_chan()
        self.admin = self.conf.get_admin()
        nl = NetLoad(self.network, self.port, self.nick, self.chan)
        self.irc = nl.conn()
        self.ml = ModLoad(self.libpath)
        self.ml.mod_load_all()

    def farg(self, arg, nick):
        """ commands """
        c = arg[4]
        cargs = []
        for x in range(5, len(arg)):
            cargs.append(arg[x])
        """ loading, unloading, reloading modules """
        for arg in loader.get_args():
            if c == arg:
                self.irc.send('PRIVMSG ' + self.chan + ' :' + getattr(loader, arg)(cargs[0], self.ml) + '\r\n')
        if c == 'gtfo' and nick == self.admin:
            self.irc.send('QUIT :Bye then...\r\n')
            exit()
        if c == 'cmds':
            clist = "Current available commands: "
            if len(self.ml.get_args()) == 0:
                clist = "No available commands.  "
            else:
                for a in self.ml.get_args():
                    clist = clist + a + ", "
            self.irc.send('PRIVMSG ' + self.chan + ' :' + clist[:-2] + '\r\n')
        for arg in self.ml.get_args():
            if c == arg:
                output = self.ml.get_arg(arg)
                self.irc.send('PRIVMSG ' + self.chan + ' :' + output + '\r\n')

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
                    self.farg(arg, ni[1:])

if __name__ == '__main__':
    bot = CBot()
    bot.run()
