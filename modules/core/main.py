def main(irc, nick, data, handler):
    if data[0][:-1] == "Gouda" and len(data) > 1:
        # message is addressed to the bot
        if data[1] == "commands":
            irc.message("You can't command me, I'm a free spirit!")
