import re
import urllib2
import os,sys
sys.path.append(os.path.abspath('../core/'))
import formatting

def cotd():
    cheese_url = "http://cheese.com"
    failed_errortext = "I was unable to find the cheese of the day."
    response = urllib2.urlopen(cheese_url)
    if response:
        cotd_url = re.search( r'<h4>Cheese of the day:</h4>.*<div class="more" onclick="location.href=\'(.*)\'">more</div>', response.read(), re.DOTALL|re.M|re.I).group(1)
        cotd_page = urllib2.urlopen(cheese_url + cotd_url)
        if cotd_page:
            cpr = cotd_page.read()
            cotd_name_match = re.search( r'<title>(.*)</title>', cpr)
            if not cotd_name_match:
                return failed_errortext + ": Error obtaining name"
            cotd_name = cotd_name_match.group(1)
            cotd_description_match = re.search( r'<meta name="description" content="(.*)"/>', cpr)
            if not cotd_description_match:
                return failed_errortext + ": Error obtaining description"
            cotd_description = cotd_description_match.group(1)
            return "The cheese of the day is " + formatting.fmat(cotd_name, "yellow") + " More Info: " + formatting.fmat(cheese_url + cotd_url, "cyan")  + "\r\n"
    return failed_errortext

def get_args():
    arglist = ["cotd"]
    return arglist
