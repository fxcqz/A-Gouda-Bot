import os
import sys
import time
import urllib2
import json
from threading import Thread
import random

""" http://stackoverflow.com/questions/11242967/python-search-with-image-google-images """

def run(term, api):
    url_list = []
    term = term.replace(' ','%20')
    count = 0
    for i in range(0,2):
        url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&start=%d&userip=MyIP' % (term, i * 4)
        request = urllib2.Request(url, None, {'Referer': 'Gouda Bot'})
        response = urllib2.urlopen(request)

        results = json.loads(response.read())
        data = results['responseData']
        data_info = data['results']

        # Iterate for each result and get unescaped url
        for u in data_info:
            count = count + 1
            url_list.append(u['unescapedUrl'])
        # Sleep for one second to prevent IP blocking from Google
        time.sleep(1)
    url_ = url_list[random.randint(0,len(url_list)-1)]
    api.message(url_)


def main(message, api):
    term = ""
    if len(message) > 1:
        term = ' '.join(w for w in message[1:])
    if term != "":
        retriever = Thread(target=run, args=(term, api))
        retriever.start()
