import importlib

class ModLoad:
    def __init__(self):
        self.arglist = {}
        self.importlist = {}

    def mod_load(self, modname):
        self.importlist[modname] = importlib.import_module(modname)
        for arg in self.importlist[modname].get_args():
            self.arglist[arg] = modname

    #def mod_load_all(self):
    #    

    def mod_reload(self, modname):
        if self.importlist[modname] != None:
            reload(self.importlist[modname])
        else:
            print "Module " + modname + " not loaded"

    def get_mod(self, modname):
        return self.importlist[modname]

    def get_args(self):
        return self.arglist

    def get_arg(self, arg):
        ret = getattr(self.importlist[self.arglist[arg]], arg)()
        return ret
