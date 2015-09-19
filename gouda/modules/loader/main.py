from gouda.utils import rreload


def load(message, api):
    module = message[1]
    if module != "loader":
        if module not in api.loader.importlist:
            api.loader.load_module(module)
            api.message("Loaded module: %s" % module)

def reload_(message, api):
    module = message[1]
    if module in api.loader.importlist:
        rreload(api.loader.importlist[module])
        api.message("Reloaded %s" % module)
    else:
        api.message("Failed to reload %s" % module)

def unload(message, api):
    module = message[1]
    if module != "loader":
        if module in api.loader.importlist:
            api.loader.unload_module(module)
            api.message("Unloaded %s" % module)
