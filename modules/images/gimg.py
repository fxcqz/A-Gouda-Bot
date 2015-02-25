import os
import sys
import time
import urllib2
import simplejson
from threading import Thread
import random

""" http://stackoverflow.com/questions/11242967/python-search-with-image-google-images """

def run(term, irc):
    if term != None:
        url_list = []
        term = term.replace(' ','%20')
        count = 0
        for i in range(0,2):
            url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+term+'&start='+str(i*4)+'&userip=MyIP')
            request = urllib2.Request(url, None, {'Referer': 'Gouda Bot'})
            response = urllib2.urlopen(request)

            results = simplejson.load(response)
            data = results['responseData']
            dataInfo = data['results']

            # Iterate for each result and get unescaped url
            for myUrl in dataInfo:
                count = count + 1
                url_list.append(myUrl['unescapedUrl'])
            # Sleep for one second to prevent IP blocking from Google
            time.sleep(1)
        irc.message(url_list[random.randint(0,len(url_list)-1)])

def arg_check(data):
    ret = False
    if data[0] == "Gouda:":
        if len(data) > 2:
            if data[1] == "image":
                ret = True
    return ret

def main(irc, nick, data, handler):
    term = ""
    if arg_check(data):
        term = ' '.join(str(x) for x in data[2:])
    else:
        # think of some reason to write a message
        term = None
    if term != "":
        retriever = Thread(target=run, args=(term,irc,))
        retriever.start()
