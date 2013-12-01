import re
import urllib2

def cotd():
    response = urllib2.urlopen("http://cheese.com")
    if response:
        m = re.search( r'style="color:.*">(.*)</a></h4>', response.read(), re.M|re.I)
        if m:
            return "The cheese of the day is " + m.group(1) + "\r\n"
    return "Unable to get cheese of the day"

def get_args():
    arglist = ["cotd"]
    return arglist
