import requests
import bs4
from .models import Tsx_losers, Tsx_gainers


def tsx_losers():
    results = requests.get('https://www.investcom.com/page/mpltoronto.htm', verify=False )
    soup = bs4.BeautifulSoup(results.text, "xml")
    div1 = soup.find_all('div', {"class": "genTable"})
    table = div1[0].find('table')
    u = table.find_all('u')
    font = table.find_all('font')
    res = {}
    if len(u) > 0:
        res[u[0].text] = [u[1].text, font[0].text, font[1].text]
    if len(u) > 2:
        res[u[2].text] = [u[3].text, font[2].text, font[3].text]
    if len(u) > 4:
        res[u[4].text] = [u[5].text, font[4].text, font[5].text]
    if len(u) > 6:
        res[u[6].text] = [u[7].text, font[6].text, font[7].text]
    if len(u) > 8:
        res[u[8].text] = [u[9].text, font[8].text, font[9].text]
    if len(u) > 10:
        res[u[10].text] = [u[11].text, font[10].text, font[11].text]
    if len(u) > 12:
        res[u[12].text] = [u[13].text, font[12].text, font[13].text]
    if len(u) > 14:
        res[u[14].text] = [u[15].text, font[14].text, font[15].text]
    print("jnjnjnjidieieiieie")
    if results.status_code == 200:
        print("dkdkdkdkkdkdkdkdkdk")
        Tsx_losers.objects.all().delete()
        for key, value in res.items():
            Tsx_losers.objects.create(symbol=key, name=value[0], change=value[1], percent=value[2])

    results = requests.get('https://www.investcom.com/page/mpgtoronto.htm', verify=False)
    soup = bs4.BeautifulSoup(results.text, "xml")
    div1 = soup.find_all('div', {"class": "genTable"})
    table = div1[0].find('table')
    u = table.find_all('u')
    font = table.find_all('font')
    res = {}
    if len(u) > 0:
        res[u[0].text] = [u[1].text, font[0].text, font[1].text]
    if len(u) > 2:
        res[u[2].text] = [u[3].text, font[2].text, font[3].text]
    if len(u) > 4:
        res[u[4].text] = [u[5].text, font[4].text, font[5].text]
    if len(u) > 6:
        res[u[6].text] = [u[7].text, font[6].text, font[7].text]
    if len(u) > 8:
        res[u[8].text] = [u[9].text, font[8].text, font[9].text]
    if len(u) > 10:
        res[u[10].text] = [u[11].text, font[10].text, font[11].text]
    if len(u) > 12:
        res[u[12].text] = [u[13].text, font[12].text, font[13].text]
    if len(u) > 14:
        res[u[14].text] = [u[15].text, font[14].text, font[15].text]

    if results.status_code == 200:
        print("hellellel gainerss   tsx")
        Tsx_gainers.objects.all().delete()
        for key, value in res.items():
            Tsx_gainers.objects.create(symbol=key, name=value[0], change=value[1], percent=value[2])
    return res


