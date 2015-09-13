def main(*args, **kwargs):
    print "lol"

def list_modules(message, api):
    api.message("Current modules: %s." % api.loader.get_modules())

def list_commands(message, api):
    api.message("Current known commands: %s." % api.loader.get_commands())
