import random
import nltk
import string

# http://www.monlp.com/2011/11/08/part-of-speech-tags/
pt_tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD",
           "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR",
           "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ",
           "WDT", "WP", "WP$", "WRB"]

def load_dictionary(path):
    wordlist = None
    try:
        with open(path, 'r') as f:
            wordlist = f.readlines()
            wordlist = [w.strip('\n') for w in wordlist]
    except IOError as e:
        print e
    return wordlist

def get_word_by_type(wtype, wordlist):
    while True:
        word = random.choice(wordlist)
        if all(c in string.printable for c in word):
            t = nltk.pos_tag([word])
            if t[0][1] in wtype:
                return word, wtype
    return None

def print_sentence(func):
    def wrapper(*args, **kwargs):
        return ' '.join([n[0] for n in func(*args, **kwargs)])
    return wrapper

@print_sentence
def sentence(pos_list, path):
    wordlist = load_dictionary(path)
    return [get_word_by_type(t, wordlist) for t in pos_list]
