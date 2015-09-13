from bs4 import BeautifulSoup


def cotd(message, api):
    data = api.web.get_page_contents("http://www.cheese.com/")
    try:
        soup = BeautifulSoup(data)
        cotd = soup.find('div', attrs={'class': 'top-offer'})\
                   .a.get('href').replace('/', '')
        api.message("The cheese of the day is %s." % cotd)
    except AttributeError:
        # no cheesy
        pass
