import urllib2

from bs4 import BeautifulSoup


class Web(object):
    def __init__(self):
        pass

    def get_page_contents(self, url):
        try:
            response = urllib2.urlopen(url)
            return response.read()
        except urllib2.HTTPError:
            pass
        return None
