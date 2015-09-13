import random
import string


# strings
MODALS = ["can", "could", "may", "might", "shall", "should", "will", "would",
          "must", "ought", "are", "am", "is", "does", "did", "didnt", "didn't",
          "do", "don't"]
GREETINGS = ["hi", "hello", "yo", "sup", "howdy", "hey"]
YES = ["yes", "yarp", "ya", "yea", "yeah duh", "yess matey", "m8... yes!!",
       "aye", "yup", "yeh", "indeedy doodly", "affirmitive", "hell yeah",
       "hells to the yeah", "yop", "fuck yeah", "y to the e to the s",
       "yes you fuckwit"]
NO = ["no", "nonononono", "nahh", "fuck that", "nope", "no way!!", "nop",
      "give me nop me mama (thats a no)", "yes... just kidding, no",
      "seriously?? no man..", "nein", "noppazor", "nuh"]


def yesno(message, api):
    api.message(random.choice([random.choice(YES), random.choice(NO)]))


def cant(message):
    str = ' '.join(message)
    cant_index = str.find("can't")
    believe_index = str.find("believe")
    if believe_index != -1 and believe_index > cant_index:
        return True
    return False


def acronym(num=3):
    letters = string.letters[:26].replace('x', random.choice('aeiou'))
    str = ""
    for x in range(num):
        str += random.choice(letters)
    return str


def main(message, api):
    if message[0] in MODALS and message[-1][-1] == '?':
        yesno(message, api)

    if any("like" in w for w in message):
        if random.randint(0, 9) == 5:
            api.message("1 like = 1 prayer x")

    elif any("lol" in w for w in message):
        if random.randint(0, 20) == 4:
            api.message("lol")

    elif message[-1] == "lo":
        api.message('l')

    elif message[-1] == "yh?":
        api.message(random.choice(YES))

    elif message[0] == "acronym":
        num = int(message[1]) if len(message) > 1 else 3
        api.message(acronym(num))

    elif message[0] in GREETINGS:
        api.message(random.choice(GREETINGS))

    elif message[0] == "bk":
        api.message("wb")

    elif "can't" in message:
        cant(message)
