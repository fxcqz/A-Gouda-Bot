import re
import urllib
import urllib2
import json
import random

url_re = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
shorten_domain = 'bitly.com'
oauthkey = 'c302a13fae88967b205cef85de65666fd65a413d'
errors = ['fuck', 'shit', 'wanker', 'bastard', 'oh bollocks', 'shitting hell', 'cunting internet']
creepy = [';)', 'no tears... only dreams now...']

def main(irc, nick, data, handler):
    print("irc: " + irc + ", nick: " + nick + ", data: " + data)
    urls = url_re.findall(data)
    print(urls)
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
                except (ValueError, httplib.HTTPException) as ex:
                    print(ex)
                    return_urls.append(random.choice(errors) + "...")
            irc.message(", ".join(return_urls))
        else:
            irc.message(random.choice(creepy))
