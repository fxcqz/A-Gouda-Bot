import re
import requests
import json
import random

url_re = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
shortern_url = 'http://www.googleapis.com/urlshortener/v1/url'
errors = ['fuck', 'shit', 'wanker', 'bastard', 'oh bollocks', 'shitting hell', 'cunting internet']
creepy = [';)', 'no tears... only dreams now...']

def main(irc, nick, data, handler):
    urls = url_re.findall(data)
    if urls:
        if "shh..." not in data:
            return_urls = []
            for url in urls:
                json_postdata = {'longUrl': url}
                try:
                    response = requests.post(shorten_url, data=json_postdata).json
                    return_urls.append(response['id'])
                except (ValueError, ConnectionError):
                    return_urls.append(random.choice(errors) + "...")
            irc.message(return_urls.join(', '))
        else
            irc.message(random.choice(creepy))
