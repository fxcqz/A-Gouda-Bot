# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import json
import random

#url_re = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[#-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
url_re = re.compile(ur'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
shorten_domain = 'bitly.com'
oauthkey = 'c302a13fae88967b205cef85de65666fd65a413d'
errors = ['fuck', 'shit', 'wanker', 'bastard', 'oh bollocks', 'shitting hell', 'cunting internet', 'blame golem']
creepy = [';)', 'no tears... only dreams now...']
min_length = 80

def main(irc, nick, data, handler):
    urls = filter(lambda x: len(x) > min_length, url_re.findall(' '.join(data)))
    if urls:
        if "shh..." not in data:
            return_urls = []
            for url in urls:
                try:
                    full_url = 'https://api-ssl.bitly.com/v3/shorten?' + urllib.urlencode({
                        'ACCESS_TOKEN': oauthkey,
                        'longUrl': url,
                    })
                    body = json.loads(urllib2.urlopen(full_url).read())
                    return_urls.append(body['data']['url'])
                except (ValueError, TypeError, urllib2.HTTPError) as ex:
                    print(ex)
                    return_urls.append(random.choice(errors) + "...")
            irc.message(" | ".join(return_urls))
        else:
            irc.message(random.choice(creepy))
