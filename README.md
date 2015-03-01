# a gouda bot

a better version of a cheese bot

dependencies:
* ConfigParser
* simplejson (optional: images module)
* bs4 (beautiful soup) (optional: cheese module)
* nltk

## modules

* directory within `modules/`
* requires `__init__.py` (see below)
* requires `main` function in one of the files
  * main function is run on every line of text received from irc *individually*
  * main takes the following parameters

> Irc - Handle to the bots irc connection
> 
> Nick - The nick of the user who sent the message
> 
> Data - The message sent to irc
> 
> Handler - Handle to the module processor. This allows use of data in other parts of the bot.

A typical `main` function could therefore be defined as such:

```python
def main(irc, nick, data, handler):
    pass
```

currently, the `main` function may not be placed inside a class.

## init.py

to be placed inside each modules directory. each init file should be very similar to the others.

the distinguishing feature of an init file it is's `mainfile` variable which is a string named as the file which contains the module's `main` function (without .py). this is used to call the `main` function declared as above.

there should also be an import which will import the file that contains the `main` function.

here is an example init file:

```python
import main
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
mainfile = "my_main_file"
```
