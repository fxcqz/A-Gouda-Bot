import operator
import moodstrings


emotions = {"happiness": 0, "sadness": 0, "surprise": 0,
            "fear": 0, "disgust": 0, "anger": 0}

def save_mood():
    with open("mood.dat", 'w') as f:
        moodstring = ""
        for key, value in emotions.iteritems():
            moodstring += key + ":" + str(value) + ","
        f.write(moodstring[:-1])
            
def load_mood():
    moodstring = ""
    try:
        with open("mood.dat", 'r') as f:
            moodstring = f.readlines()
    except IOError:
        print "mood went wrong"
        moodstring = ["happiness:0,sadness:0,surprise:0,fear:0,disgust:0,anger:0"]
    moodstring = moodstring[0].split(",")
    for m in moodstring:
        emotion = m.split(":")
        emotions[emotion[0]] = int(emotion[1])

def emotions_equal():
    e = 0
    for key, value in emotions.iteritems():
        if value != e:
            return False
        e = value
    return True

def state_mood():
    load_mood()
    message = "I have stable feelings"
    if not emotions_equal():
        max_emotion = max(emotions.iteritems(), key=operator.itemgetter(1))[0]
        if max_emotion == "sadness":
            message = "Sad (" + str(emotions["sadness"]) + ")"
        elif max_emotion == "happiness":
            message = "Happy (" + str(emotions["happiness"]) + ")"
        elif max_emotion == "surprise":
            message = "Surprised (" + str(emotions["surprise"]) + ")"
        elif max_emotion == "fear":
            message = "Fearful (" + str(emotions["fear"]) + ")"
        elif max_emotion == "disgust":
            message = "Disgusted (" + str(emotions["disgust"]) + ")"
        elif max_emotion == "anger":
            message = "Angry (" + str(emotions["anger"]) + ")"
    return message

def main(irc, nick, data, handler):
    reload(moodstrings)
    offset = 0
    if data[0] == "Gouda:":
        offset = 1
    if len(data[offset:]) > 0:
        msg = ' '.join(data[offset:])
        if msg == "mood":
            irc.message(state_mood())
        for key, value in moodstrings.moodstrings.iteritems():
            for v in value:
                if msg == v:
                    emotions[key] += 1
                    save_mood()
