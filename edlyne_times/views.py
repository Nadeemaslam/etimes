from django.shortcuts import render
from nsetools import Nse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from yahoo_fin import stock_info as si
from pandas import DataFrame
import json
import time

import asyncio
from asgiref.sync import sync_to_async


@sync_to_async
def get_nasdaq_gainers_async():
    nasdaq_gainers = si.get_day_gainers().head(5)
    nasdaq_gainers.columns = nasdaq_gainers.columns.str.replace(' ', '')
    nasdaq_gainers.columns = nasdaq_gainers.columns.str.replace('[#,@,&]', '')
    nasdaq_gainers.rename(columns={'Price(Intraday)': 'Price', '%Change': 'per_change'}, inplace=True)
    nasdaq_gainers_json_records = DataFrame(nasdaq_gainers,
                                            columns=['Symbol', 'Name', 'Price', 'per_change', 'Volume']).to_json(
        orient='records')
    nasdaq_gainers = []
    nasdaq_gainers = json.loads(nasdaq_gainers_json_records)
    return nasdaq_gainers


@sync_to_async
def get_nasdaq_losers_async():
    nasdaq_losers = si.get_day_losers().head(5)
    nasdaq_losers.columns = nasdaq_losers.columns.str.replace(' ', '')
    nasdaq_losers.columns = nasdaq_losers.columns.str.replace('[#,@,&]', '')
    nasdaq_losers.rename(columns={'Price(Intraday)': 'Price', '%Change': 'per_change'}, inplace=True)
    nasdaq_losers.rename(columns={'Price(Intraday)': 'Price'}, inplace=True)
    nasdaq_losers_json_records = DataFrame(nasdaq_losers,
                                           columns=['Symbol', 'Name', 'Price', 'per_change', 'Volume']).to_json(
        orient='records')
    nasdaq_losers = []
    nasdaq_losers = json.loads(nasdaq_losers_json_records)
    return nasdaq_losers


@sync_to_async
def get_nse_gainers_async():
    nse = Nse()
    nse_gainers = nse.get_top_gainers()
    return nse_gainers


@sync_to_async
def get_nse_losers_async():
    nse = Nse()
    nse_losers = nse.get_top_losers()
    return nse_losers

async  def index(request):
    start_time = time.time()
    task1 = asyncio.ensure_future(get_nasdaq_gainers_async())
    task2 = asyncio.ensure_future(get_nasdaq_losers_async())
    # task3 = asyncio.ensure_future(get_nse_gainers_async())
    # task4 = asyncio.ensure_future(get_nse_losers_async())
    await asyncio.wait([task1, task2])

    context = {'nasdaq_gainers': task1.result(), 'nasdaq_losers': task2.result()}
    print(time.time() - start_time)
    return render(request, 'edlyne_times/index.html', context)








def research(request):
    context = {}
    return render(request, 'edlyne_times/research.html', context)



def nse(request):

    # nse = Nse()
    # data = nse.get_top_gainers()
    # context = {'companyName': data[0]['symbol'],'LTP': data[1]['ltp']}
     # print( data(i), print (data[0]['symbol'],"llllll", data[1]['ltp']))
    return render(request, 'edlyne_times/nse.html', )



