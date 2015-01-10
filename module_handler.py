import sys
import importlib
import inspect

class ModuleHandler:
    def __init__(self, path, irc):
        self.path = path
        self.importlist = {}
        self.status = ""
        self.delayed_imports = []
        self.delayed_unloads = []
        self.irc = irc

    def unload_module(self, name, delay=True):
        try:
            if delay == True:
                self.delayed_unloads.append(name)
            else:
                if self.importlist[name] != None:
                    del self.importlist[name]
        except KeyError:
            pass

    def load_module(self, name, delay=True, startup=False):
        if delay == True:
            self.delayed_imports.append(name)
        else:
            print "loading", name
            self.status = ""
            name = name.replace("\r\n", "")
            if name not in self.importlist:
                try:
                    handle = importlib.import_module("modules."+name)
                    main = importlib.import_module("modules."+name+"."+handle.mainfile)
                    getattr(main, "main")
                    self.status = "Loaded module: " + name
                    self.importlist[name] = main
                    if startup == False:
                        self.irc.message("Loaded module: " + name)
                except:
                    self.status = "Failed to load " + name
                    if startup == False:
                        self.irc.message("Failed to load: " + name)
            else:
                if startup == False:
                    self.irc.message(name + " is already loaded")
