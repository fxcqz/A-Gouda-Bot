import importlib
import os, sys

class ModLoad:
    def __init__(self, libpath):
        self.arglist = {}
        self.importlist = {}
        self.lpath = libpath

    def mod_load(self, modname):
        self.importlist[modname] = importlib.import_module(modname)
        try:
            for arg in self.importlist[modname].get_args():
                if arg in self.arglist:
                    print "Command already exists!"
                else:
                    self.arglist[arg] = modname
        except AttributeError:
            print "No arg list found"

    def mod_load_all(self):
        dirs = os.listdir(self.lpath+"modules/")
        for x in range(len(dirs)):
            if dirs[x][-3:] != "pyc" and dirs[x][-3:] != ".py":
                for root, directories, files in os.walk(self.lpath+"modules/"+dirs[x]):
                    sys.path.append(os.path.abspath(self.lpath+'modules/'+dirs[x]))
                    for filename in files:
                        try:
                            if filename[-3:] == ".py":
                                ret = getattr(importlib.import_module(filename[:-3]), "get_args")()
                                if type(ret) is list:
                                    self.mod_load(filename[:-3])
                        except AttributeError:
                            pass

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
        try:
            ret = getattr(self.importlist[self.arglist[arg]], arg)()
        except AttributeError:
            ret = "No function found"
        return ret
