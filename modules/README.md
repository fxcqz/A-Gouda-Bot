Modules
-------

New directory for each module (for clarity).

Requirements for a module:

1. At least one .py file with a get_args() function in it.
2. get_args() must return a list of strings which you want to be commands for the bot.
3. If a function is going to output for a command, it must have the same name as the command.

Example
-------

    def hello():
        return "Hello there"

    def get_args():
        arglist = ["hello"]
        return arglist

Then running the bot:

    <@nick> Gouda: hello
    < Gouda> Hello there
