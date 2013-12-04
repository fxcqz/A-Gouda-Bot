import importlib
import os

class ModLoad:
    def __init__(self, libpath):
        self.arglist = {}
        self.importlist = {}
        self.lpath = libpath

    def mod_load(self, modname):
        self.importlist[modname] = importlib.import_module(modname)
        for arg in self.importlist[modname].get_args():
            if arg in self.arglist:
                print "Command already exists!"
            else:
                self.arglist[arg] = modname

    def mod_load_all(self):
        flist = os.listdir(self.lpath + "modules")
        for f in flist:
            if f[-3:] == ".py":
                # only need .py files
                self.mod_load(f[:-3])

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
