from django.shortcuts import render
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from edlyne_times.models import report
import bs4
import requests
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import Post
from .models import Tsx_losers, Tsx_gainers
from .models import Nyse_gainers, Nyse_losers
from .models import Nasdaq_gainers, Nasdaq_losers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_nasdaq_gainers(request):
    res = requests.get('https://munafasutra.com/nasdaq/top/GAINERS/Day', verify=False)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find_all('table')
    td = table[1].find_all('td')
    #
    res = {}
    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[7].text, td[6].text, td[5].text[:-7]]
        text = td[5].text
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[11].text, td[10].text, td[9].text[:-7]]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[15].text, td[14].text, td[13].text[:-7]]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[19].text, td[18].text, td[17].text[:-7]]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[23].text, td[22].text, td[21].text[:-7]]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[27].text, td[26].text, td[25].text[:-7]]
    return JsonResponse(res)


def get_nasdaq_losers(request):
    res = requests.get('https://munafasutra.com/nasdaq/top/LOSERS/Day',  verify=False)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find_all('table')
    td = table[1].find_all('td')

    res = {}
    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[7].text, td[6].text, td[5].text[:-7]]
        text = td[5].text
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[11].text, td[10].text, td[9].text[:-7]]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[15].text, td[14].text, td[13].text[:-7]]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[19].text, td[18].text, td[17].text[:-7]]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[23].text, td[22].text, td[21].text[:-7]]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[27].text, td[26].text, td[25].text[:-7]]
    return JsonResponse(res)


def nyse_gainers(request):
    results = requests.get('https://munafasutra.com/nyse/top/GAINERS/Day', verify=False)
    soup = bs4.BeautifulSoup(results.text, "lxml")
    table = soup.find_all('table')
    td = table[1].find_all('td')
    #
    res = {}

    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[7].text, td[6].text, td[5].text[:-7]]
        text = td[5].text
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[11].text, td[10].text, td[9].text[:-7]]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[15].text, td[14].text, td[13].text[:-7]]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[19].text, td[18].text, td[17].text[:-7]]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[23].text, td[22].text, td[21].text[:-7]]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[27].text, td[26].text, td[25].text[:-7]]

    return JsonResponse(res)



def nyse_losers(request):
    results = requests.get('https://munafasutra.com/nyse/top/LOSERS/Day', verify=False)
    soup = bs4.BeautifulSoup(results.text, "lxml")
    table = soup.find_all('table')
    td = table[1].find_all('td')

    res = {}

    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[7].text, td[6].text, td[5].text[:-7]]
        text = td[5].text
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[11].text, td[10].text, td[9].text[:-7]]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[15].text, td[14].text, td[13].text[:-7]]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[19].text, td[18].text, td[17].text[:-7]]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[23].text, td[22].text, td[21].text[:-7]]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[27].text, td[26].text, td[25].text[:-7]]

    return JsonResponse(res)


def tsx_gainers(request):

    results = requests.get('https://www.investcom.com/page/mpgtoronto.htm', verify=False)
    soup = bs4.BeautifulSoup(results.text,"xml")
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

    return JsonResponse(res)

def tsx_losers(request):
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

    return JsonResponse(res)



def home(request):
    blogs = Post.objects.filter(status=1).order_by('-created_on')[:10]
    tsx_losers = Tsx_losers.objects.all()
    tsx_gainers = Tsx_gainers.objects.all()
    nyse_gainers = Nyse_gainers.objects.all()
    nyse_losers = Nyse_losers.objects.all()
    nasdaq_gainers = Nasdaq_gainers.objects.all()
    nasdaq_losers = Nasdaq_losers.objects.all()
    context = {'Post': blogs, 'tsx_losers': tsx_losers, 'tsx_gainers': tsx_gainers,
               'nyse_gainers': nyse_gainers, 'nyse_losers': nyse_losers,
               'nasdaq_gainers': nasdaq_gainers, 'nasdaq_losers': nasdaq_losers}
    return render(request, 'edlyne_times/index.html', context)

def nse(request):


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
    stocks = report.objects.filter(exchange=exchange, category=user_group).order_by('-created_on')
    context = {'range': stocks, 'user_group': user_group}
    return render(request, 'edlyne_times/research.html', context)


def services(request):
    return render(request, 'edlyne_times/services.html')



def products(request, exchange):

    user_category = request.user.groups.all().values()
    nse_gold, nse_dividend, nse_health, nse_platinum, nse_penny, nse_technical, nse_american,nse_ipo, nse_resources, \
    bse_gold, bse_dividend, bse_health, bse_platinum, bse_penny, bse_technical, bse_american, bse_resources, bse_ipo,\
    nyse_gold, nyse_dividend, nyse_health, nyse_platinum, nyse_penny, nyse_technical, nyse_american, nyse_resources, nyse_ipo,\
    nasdaq_gold, nasdaq_dividend, nasdaq_health, nasdaq_platinum, nasdaq_ipo, \
    nasdaq_penny, nasdaq_technical, nasdaq_american, nasdaq_resources, tsx_ipo,\
    tsx_gold, tsx_dividend, tsx_health, tsx_platinum, tsx_penny, tsx_technical, tsx_american, tsx_resources, = (False,)*45

    for key in user_category:
        if key['name'] == 'nse_gold':
            nse_gold = True
        elif key['name'] == 'nse_dividend':
            nse_dividend = True
        elif key['name'] == 'nse_health':
            nse_health = True
        elif key['name'] == 'nse_platinum':
            nse_platinum = True
        elif key['name'] == 'nse_penny':
            nse_penny = True
        elif key['name'] == 'nse_technical':
            nse_technical = True
        elif key['name'] == 'nse_resources':
            nse_resources = True
        elif key['name'] == 'nse_american':
            nse_american = True
        elif key['name'] == 'nse_ipo':
            nse_ipo = True
        elif key['name'] == 'bse_gold':
            bse_gold = True
        elif key['name'] == 'bse_ipo':
            bse_ipo = True
        elif key['name'] == 'bse_dividend':
            bse_dividend = True
        elif key['name'] == 'bse_health':
            bse_health = True
        elif key['name'] == 'bse_platinum':
            bse_platinum = True
        elif key['name'] == 'bse_penny':
            bse_penny = True
        elif key['name'] == 'bse_technical':
            bse_technical = True
        elif key['name'] == 'bse_resources':
            bse_resources = True
        elif key['name'] == 'bse_american':
            bse_american = True
        elif key['name'] == 'nasdaq_gold':
            nasdaq_gold = True
        elif key['name'] == 'nasdaq_ipo':
            nasdaq_ipo = True
        elif key['name'] == 'nasdaq_dividend':
            nasdaq_dividend = True
        elif key['name'] == 'nasdaq_health':
            nasdaq_health = True
        elif key['name'] == 'nasdaq_platinum':
            nasdaq_platinum = True
        elif key['name'] == 'nasdaq_penny':
            nasdaq_penny = True
        elif key['name'] == 'nasdaq_technical':
            nasdaq_technical = True
        elif key['name'] == 'nasdaq_resources':
            nasdaq_resources = True
        elif key['name'] == 'nasdaq_american':
            nasdaq_american = True
        elif key['name'] == 'tsx_gold':
            tsx_gold = True
        elif key['name'] == 'tsx_ipo':
            tsx_ipo = True
        elif key['name'] == 'tsx_dividend':
            tsx_dividend = True
        elif key['name'] == 'tsx_health':
            tsx_health = True
        elif key['name'] == 'tsx_platinum':
            tsx_platinum = True
        elif key['name'] == 'tsx_penny':
            tsx_penny = True
        elif key['name'] == 'tsx_technical':
            tsx_technical = True
        elif key['name'] == 'tsx_resources':
            tsx_resources = True
        elif key['name'] == 'tsx_american':
            tsx_american = True
        elif key['name'] == 'nyse_gold':
            nyse_gold = True
        elif key['name'] == 'nyse_dividend':
            nyse_dividend = True
        elif key['name'] == 'nyse_health':
            nyse_health = True
        elif key['name'] == 'nyse_platinum':
            nyse_platinum = True
        elif key['name'] == 'nyse_penny':
            nyse_penny = True
        elif key['name'] == 'nyse_technical':
            nyse_technical = True
        elif key['name'] == 'nyse_resources':
            nyse_resources = True
        elif key['name'] == 'nyse_american':
            nyse_american = True
        elif key['name'] == 'nyse_ipo':
            nyse_ipo = True
    exchange = exchange
    context = {'exchange': exchange, 'nse_gold': nse_gold, 'nse_dividend': nse_dividend,
               'nse_health': nse_health, 'nse_penny': nse_penny, 'nse_resources': nse_resources, 'nse_platinum': nse_platinum,
               'nse_technical': nse_technical, 'nse_american': nse_american,'nse_ipo': nse_ipo,
               'bse_gold': bse_gold, 'bse_dividend': bse_dividend,
               'bse_health': bse_health, 'bse_penny': bse_penny, 'bse_resources': bse_resources,
               'bse_platinum': bse_platinum, 'nyse_ipo': nyse_ipo,
               'bse_technical': bse_technical, 'bse_american': bse_american,
               'nyse_gold': nyse_gold, 'nyse_dividend': nyse_dividend,'bse_ipo': bse_ipo,
               'nyse_health': nyse_health, 'nyse_penny': nyse_penny, 'nyse_resources': nyse_resources,
               'nyse_platinum': nyse_platinum,'nyse_ipo': nyse_ipo,
               'nyse_technical': nyse_technical, 'nyse_american': nyse_american,
               'nasdaq_gold': nasdaq_gold, 'nasdaq_dividend': nasdaq_dividend,
               'nasdaq_health': nasdaq_health, 'nasdaq_penny': nasdaq_penny, 'nasdaq_resources': nasdaq_resources,
               'nasdaq_platinum': nasdaq_platinum,'nasdaq_ipo': nasdaq_ipo,
               'nasdaq_technical': nasdaq_technical, 'nasdaq_american': nasdaq_american,
               'tsx_gold': tsx_gold, 'tsx_dividend': tsx_dividend,'tsx_ipo': tsx_ipo,
               'tsx_health': tsx_health, 'tsx_penny': tsx_penny, 'tsx_resources': tsx_resources,
               'tsx_platinum': tsx_platinum,
               'tsx_technical': tsx_technical, 'tsx_american': tsx_american
               }
    return render(request, 'edlyne_times/products.html', context)


def get_bse_gainers(request):
    res = requests.get('https://money.rediff.com/gainers/bse', verify=False )
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find('table', {"class": "dataTable"})
    td = table.find_all('td')

    res = {}
    if len(td) > 0:
        res[td[0].text.lstrip()] = [td[2].text, td[3].text, td[4].text]
    if len(td) > 5:
        res[td[5].text.lstrip()] = [td[7].text, td[8].text, td[9].text]
    if len(td) > 10:
        res[td[10].text.lstrip()] = [td[12].text, td[13].text, td[14].text]
    if len(td) > 15:
        res[td[15].text.lstrip()] = [td[17].text, td[18].text, td[19].text]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[22].text, td[23].text, td[24].text]
    if len(td) > 25:
        res[td[25].text.lstrip()] = [td[27].text, td[28].text, td[29].text]
    if len(td) > 30:
        res[td[30].text.lstrip()] = [td[32].text, td[33].text, td[34].text]
    if len(td) > 35:
        res[td[35].text.lstrip()] = [td[37].text, td[38].text, td[39].text]

    return JsonResponse(res)

def get_bse_losers(request):
    res = requests.get('https://money.rediff.com/losers/bse/daily', verify=False)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find('table', {"class": "dataTable"})
    td = table.find_all('td')

    res = {}
    if len(td) > 0:
        res[td[0].text.lstrip()] = [td[2].text, td[3].text, td[4].text]
    if len(td) > 5:
        res[td[5].text.lstrip()] = [td[7].text, td[8].text, td[9].text]
    if len(td) > 10:
        res[td[10].text.lstrip()] = [td[12].text, td[13].text, td[14].text]
    if len(td) > 15:
        res[td[15].text.lstrip()] = [td[17].text, td[18].text, td[19].text]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[22].text, td[23].text, td[24].text]
    if len(td) > 25:
        res[td[25].text.lstrip()] = [td[27].text, td[28].text, td[29].text]
    if len(td) > 30:
        res[td[30].text.lstrip()] = [td[32].text, td[33].text, td[34].text]
    if len(td) > 35:
        res[td[35].text.lstrip()] = [td[37].text, td[38].text, td[39].text]
    return JsonResponse(res)



def get_nse_gainers(request):
    res = requests.get('https://money.rediff.com/gainers/nse', verify=False)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find('table', {"class": "dataTable"})
    td = table.find_all('td')

    res = {}
    if len(td) > 0:
        res[td[0].text.lstrip()] = [td[1].text, td[2].text, td[3].text]
    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[5].text, td[6].text, td[7].text]
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[9].text, td[10].text, td[11].text]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[13].text, td[14].text, td[15].text]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[17].text, td[18].text, td[19].text]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[21].text, td[22].text, td[23].text]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[25].text, td[26].text, td[27].text]
    if len(td) > 28:
        res[td[28].text.lstrip()] = [td[29].text, td[30].text, td[31].text]
    return JsonResponse(res)

def get_nse_losers(request):
    res = requests.get('https://money.rediff.com/losers/nse/daily', verify=False)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    table = soup.find('table', {"class": "dataTable"})
    td = table.find_all('td')

    res = {}
    if len(td) > 0:
        res[td[0].text.lstrip()] = [td[1].text, td[2].text, td[3].text]
    if len(td) > 4:
        res[td[4].text.lstrip()] = [td[5].text, td[6].text, td[7].text]
    if len(td) > 8:
        res[td[8].text.lstrip()] = [td[9].text, td[10].text, td[11].text]
    if len(td) > 12:
        res[td[12].text.lstrip()] = [td[13].text, td[14].text, td[15].text]
    if len(td) > 16:
        res[td[16].text.lstrip()] = [td[17].text, td[18].text, td[19].text]
    if len(td) > 20:
        res[td[20].text.lstrip()] = [td[21].text, td[22].text, td[23].text]
    if len(td) > 24:
        res[td[24].text.lstrip()] = [td[25].text, td[26].text, td[27].text]
    if len(td) > 28:
        res[td[28].text.lstrip()] = [td[29].text, td[30].text, td[31].text]
    return JsonResponse(res)



def PostList(request):
    blogs = Post.objects.filter(status=1).order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(blogs, 4)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {'Post': blogs}
    return render(request, 'edlyne_times/post.html', context)



def PostDetail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        blogs = Post.objects.filter(status=1).order_by('-created_on')[:3]
        context = {'blogs': blogs, 'post': post}
        return render(request, 'edlyne_times/post_detail.html', context)
    except ObjectDoesNotExist:
        return render(request, 'edlyne_times/post_detail.html')


def about(request):
    return render(request, 'edlyne_times/about.html')
