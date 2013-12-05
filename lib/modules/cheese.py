import re
import urllib2
import os,sys
sys.path.append(os.path.abspath('../core/'))
import formatting
__last_cheese = dict()

def cotd():
    global __last_cheese
    cheese_url = "http://cheese.com"
    failed_errortext = "I was unable to find the cheese of the day."
    response = urllib2.urlopen(cheese_url)
    if response:
        cotd_url = re.search( r'<h4>Cheese of the day:</h4>.*<div class="more" onclick="location.href=\'(.*)\'">more</div>', response.read(), re.DOTALL|re.M|re.I).group(1)
        cotd_page = urllib2.urlopen(cheese_url + cotd_url)
        if cotd_page:
            cpr = cotd_page.read()
            cotd_name_match = re.search( r'<title>(.*) - Cheese.com</title>', cpr)
            if not cotd_name_match:
                return failed_errortext + ": Error obtaining name"
            cotd_name = cotd_name_match.group(1)
            cotd_description_match = re.search( r'<meta name="description" content="(.*)"/>', cpr)
            if not cotd_description_match:
                return failed_errortext + ": Error obtaining description"
            cotd_description = cotd_description_match.group(1)
            if not '__last_cheese' in globals():
                __last_cheese = dict()
            __last_cheese["name"] = cotd_name
            __last_cheese["description"] = cotd_description
            return formatting.fmat_tags("The cheese of the day is [yellow][bold]" + cotd_name +  "[clear] More Info: [cyan][bold][underline]" + cheese_url + cotd_url  + "[clear](Alternatively, use 'cotd_more'.\r\n")
    return failed_errortext

def cotd_more():
    if '__last_cheese' in globals() and 'name' in __last_cheese.keys() and 'description' in __last_cheese.keys():
        cheese_text = __last_cheese["name"] + ": " + __last_cheese["description"]
        __last_cheese.clear()
        return cheese_text
    else:
        return "More? More what!? Use 'cotd' for the cheese of the day."

def get_args():
    arglist = ["cotd", "cotd_more"]
    return arglist
