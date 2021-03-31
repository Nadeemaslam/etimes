from django.shortcuts import render
from nsetools import Nse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from yahoo_fin import stock_info as si
from pandas import DataFrame
import json

def index(request):
    nasdaq_gainers = si.get_day_gainers().head()
    nasdaq_gainers.columns = nasdaq_gainers.columns.str.replace(' ', '')
    nasdaq_gainers.columns = nasdaq_gainers.columns.str.replace('[#,@,&]', '')
    nasdaq_gainers.rename(columns={'Price(Intraday)': 'Price'}, inplace=True)
    nasdaq_gainers_json_records = DataFrame(nasdaq_gainers, columns=['Symbol', 'Name', 'Price', 'Change', 'Volume']).to_json(orient='records')
    nasdaq_gainers = []
    nasdaq_gainers = json.loads(nasdaq_gainers_json_records)

    nasdaq_losers = si.get_day_losers().head()
    nasdaq_losers.columns = nasdaq_losers.columns.str.replace(' ', '')
    nasdaq_losers.columns = nasdaq_losers.columns.str.replace('[#,@,&]', '')
    nasdaq_losers.rename(columns={'Price(Intraday)': 'Price'}, inplace=True)
    nasdaq_losers_json_records = DataFrame(nasdaq_losers, columns=['Symbol', 'Name', 'Price', 'Change', 'Volume']).to_json(orient='records')
    nasdaq_losers = []
    nasdaq_losers = json.loads(nasdaq_losers_json_records)
    print(nasdaq_losers)

    nse = Nse()
    gainers = nse.get_top_gainers()
    losers = nse.get_top_losers

    context = {'gainers': gainers, 'losers': losers, 'nasdaq_gainers': nasdaq_gainers, 'nasdaq_losers': nasdaq_losers}
    return render(request, 'edlyne_times/index.html', context)


def research(request):
    context = {}
    return render(request, 'edlyne_times/research.html', context)



def nse(request):

    nse = Nse()
    data = nse.get_top_gainers()
    context = {'companyName': data[0]['symbol'],'LTP': data[1]['ltp']}
     # print( data(i), print (data[0]['symbol'],"llllll", data[1]['ltp']))
    return render(request, 'edlyne_times/nse.html', {'data':data})



