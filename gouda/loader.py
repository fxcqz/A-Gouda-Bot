import importlib


class Loader(object):
    def __init__(self, api, settings):
        self.api = api
        self.importlist = {}
        self.api.importlist = self.importlist
        self.delayed_imports = []
        self.delayed_unloads = []
        self.settings = settings
        self.init_load()

    def init_load(self):
        for module in self.settings.modules:
            self.load_module(module, False)

    def load_module(self, name, delay=True):
        name = name.replace("\r\n", "")
        if delay is True:
            self.delayed_imports.append(name)
        else:
            if name not in self.importlist:
                try:
                    handle = importlib.import_module("gouda.modules.%s" % name)
                    if hasattr(handle, "META") or hasattr(handle, "mainfile"):
                        self.importlist[name] = handle
                        # "inject" the api into the module
                        setattr(self.importlist[name], 'api', self.api)
                except Exception as e:
                    print "IMPORT ERROR:", e

    def do_imports(self):
        for module in self.delayed_imports:
            self.load_module(module, False)
            self.delayed_imports.remove(module)

    def unload_module(self, name, delay=True):
        name = name.replace("\r\n", "")
        try:
            if delay is True:
                self.delayed_unloads.append(name)
            else:
                if self.importlist[name] is not None:
                    del self.importlist[name]
        except KeyError:
            # module isnt loaded anyway
            pass

    def do_unloads(self):
        for module in self.delayed_unloads:
            self.unload_module(module, False)
            self.delayed_unloads.remove(module)

    def get_modules(self):
        if self.importlist:
            return ', '.join(k for k in self.importlist)
        return "No modules loaded."

    def get_commands(self):
        cmds = []
        for name, module in self.importlist.iteritems():
            try:
                for cmd in module.META['commands']:
                    cmds.append(cmd)
            except KeyError:
                pass
        if len(cmds) == 0:
            return "None."
        return ', '.join(cmds)
