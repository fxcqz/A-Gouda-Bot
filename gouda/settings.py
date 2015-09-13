import json


class Settings(object):
    def __init__(self, file):
        with open(file, 'r') as handle:
            self.data = json.loads(handle.read())

        for key in self.data:
            setattr(self, key, self.data[key])

        if self.core['channel'][0] != '#':
            self.core['channel'] = '#' + self.core['channel']

    @property
    def names(self):
        return self.core['username'], self.core['hostname'],\
               self.core['servername'], self.core['realname']

    @property
    def connect(self):
        return self.network['server'], self.network['port']

    @property
    def ircinit(self):
        return self.core['nick'], self.core['channel'], self.names
