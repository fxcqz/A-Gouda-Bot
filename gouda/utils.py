from threading import Thread
import time
from types import ModuleType


class Join(object):
    """
    Decorator for joining an irc server when Gouda is run.
    """
    def __init__(self, function):
        self.function = function

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            instance.irc.connect(instance.settings.connect)
            Thread(target=lambda: [time.sleep(3), instance.irc.join()]).start()
            return self.function(instance, *args, **kwargs)
        return wrapper


def rreload(module):
    """Recursively reload modules."""
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)
