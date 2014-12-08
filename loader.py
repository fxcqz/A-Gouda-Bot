import importlib
def load(mod, ml):
    retstr = ""
    ml.mod_load(mod)
    try:
        getattr(importlib.import_module(mod), "get_args")
        retstr = "\001ACTION loaded module " + mod + "\001"
    except AttributeError:
        retstr = "\001ACTION was unable to load " + mod + "\001"
    return retstr

def unload(mod, ml):
    dlist = []
    for key, val in ml.arglist.iteritems():
        if val == mod:
            dlist.append(key)
    for x in dlist:
        del ml.arglist[x]
    return "\001ACTION unloaded module " + mod + "\001"

def reload(mod, ml):
    ml.mod_reload(mod)
    return "\001ACTION reloaded module " + mod + "\001"

def get_args():
    arglist = ["load", "unload", "reload"]
    return arglist
