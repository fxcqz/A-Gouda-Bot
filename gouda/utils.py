from threading import Thread
import time


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
