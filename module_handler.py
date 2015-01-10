import sys
import importlib
import inspect

class ModuleHandler:
    def __init__(self, path):
        self.path = path
        self.importlist = {}
        self.status = ""
        self.delayed_imports = []
        self.delayed_unloads = []

    def unload_module(self, name, delay=True):
        try:
            if delay == True:
                self.delayed_unloads.append(name)
            else:
                if self.importlist[name] != None:
                    del self.importlist[name]
        except KeyError:
            pass

    def load_module(self, name, delay=True):
        if delay == True:
            self.delayed_imports.append(name)
        else:
            print "loading", name
            self.status = ""
            name = name.replace("\r\n", "")
            try:
                handle = importlib.import_module("modules."+name)
                main = importlib.import_module("modules."+name+"."+handle.mainfile)
                getattr(main, "main")
                self.status = "Loaded module: " + name
                self.importlist[name] = main
            except:
                self.status = "Failed to load " + name
                print self.status
