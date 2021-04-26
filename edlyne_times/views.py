from django.shortcuts import render
from nsetools import Nse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import time
from edlyne_times.models import report
import asyncio
from asgiref.sync import sync_to_async
import bs4
import requests
from accounts.decorators import allowed_users
from django.shortcuts import redirect



@sync_to_async
def get_nasdaq_gainers_async():


    res = requests.get('https://www.investcom.com/us/mpgnasdaq.htm')
    soup = bs4.BeautifulSoup(res.text,"xml")
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
    return res


@sync_to_async
def get_nasdaq_losers_async():
    res = requests.get('https://www.investcom.com/us/mplnasdaq.htm')
    soup = bs4.BeautifulSoup(res.text, "xml")
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
    return res


@sync_to_async
def get_nyse_gainers_async():


    res = requests.get('https://www.investcom.com/us/mpgnyse.htm')
    soup = bs4.BeautifulSoup(res.text, "xml")
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
    return res


@sync_to_async
def get_nyse_losers_async():
    res = requests.get('https://www.investcom.com/us/mplnyse.htm')
    soup = bs4.BeautifulSoup(res.text, "xml")
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
    return res



@sync_to_async
def get_nse_gainers_async():
    nse = Nse()
    nse_gainers = nse.get_top_gainers()
    return nse_gainers


@sync_to_async
def get_tsx_gainers_async():


    res = requests.get('https://www.investcom.com/page/mpgtoronto.htm')
    soup = bs4.BeautifulSoup(res.text,"xml")
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

    return res

@sync_to_async
def get_tsx_losers_async():
    res = requests.get('https://www.investcom.com/page/mpltoronto.htm')
    soup = bs4.BeautifulSoup(res.text, "xml")
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
    return res

@sync_to_async
def get_nse_losers_async():
    nse = Nse()
    nse_losers = nse.get_top_losers()
    return nse_losers

async  def index(request):
    start_time = time.time()
    task1 = asyncio.ensure_future(get_nasdaq_gainers_async())
    task2 = asyncio.ensure_future(get_nasdaq_losers_async())
    task3 = asyncio.ensure_future(get_nyse_gainers_async())
    task4 = asyncio.ensure_future(get_nyse_losers_async())
    task5 = asyncio.ensure_future(get_tsx_gainers_async())
    task6 = asyncio.ensure_future(get_tsx_losers_async())
    await asyncio.wait([task1, task2, task3, task4, task5, task6])

    context = {'nasdaq_gainers': task1.result(), 'nasdaq_losers': task2.result(),
               'nyse_gainers': task3.result(), 'nyse_losers': task4.result(),
               'tsx_gainers': task5.result(), 'tsx_losers': task6.result()}
    print(time.time() - start_time)
    return render(request, 'edlyne_times/index.html', context)



def nse(request):

    # nse = Nse()
    # data = nse.get_top_gainers()
    # context = {'companyName': data[0]['symbol'],'LTP': data[1]['ltp']}
     # print( data(i), print (data[0]['symbol'],"llllll", data[1]['ltp']))
    return render(request, 'edlyne_times/nse.html', )

def reports(request, slug):
    logged_user = request.GET.get('user_group', -1)
    user_category = list(request.user.groups.all().values())
    allowed_group = []
    for user in user_category:
        allowed_group.append(user['name'])
    if logged_user in allowed_group:
        stock_report = report.objects.get(slug=slug)
        return render(request, 'edlyne_times/stock_report.html', {'stock_report': stock_report})
    else:
        return redirect('contact')


def research(request, exchange):
    user_group = request.GET.get('user_group', -1)
    stocks = report.objects.filter(exchange=exchange, category='user_group')
    context = {'range': stocks, 'user_group': user_group}
    return render(request, 'edlyne_times/research.html', context)

@allowed_users(allowed_roles=['admin', 'basic', 'gold'])
def products(request, exchange):

    user_category = request.user.groups.all().values()
    gold = False
    dividend = False
    health = False
    penny = False
    resources = False
    platinum = False
    for key in user_category:
        if key['name'] == 'gold':
            gold = True
        elif key['name'] =='dividend':
            dividend = True
        elif key['name'] =='health':
            health = True
        elif key['name'] =='platinum':
            platinum = True
        elif key['name'] =='penny':
            penny = True
        elif key['name'] =='resources':
            resources = True
    exchange = exchange
    context = {'exchange': exchange, 'gold': gold, 'dividend': dividend,
               'health': health, 'penny': penny, 'resources': resources, 'platinum':platinum}
    return render(request, 'edlyne_times/products.html', context)



