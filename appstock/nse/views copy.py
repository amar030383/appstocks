from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from nse.NSE_SupportFunction import *
import json, time
from datetime import date, timedelta

def getNSE_StocksDaily(request):
    data= GetStocksAngelOne.objects.all().distinct()
    loop = 0
    for stock in data:
        d= (stock.name)
        loop=loop+1
        print (d, loop)
        data = nse.get_quote(d)
        pricebandupper = data['pricebandupper']
        symbol = data['symbol']
        companyName=data['companyName']
        marketType=data['marketType'],
        dayHigh=data['dayHigh']
        basePrice=data['basePrice']
        pricebandlower=data['pricebandlower']
        dayLow=data['dayLow']
        pChange=data['pChange']
        averagePrice=data['averagePrice']
        cm_ffm=data['cm_ffm']
        high52=data['high52']
        previousClose=data['previousClose']
        low52=data['low52']
        priceBand=data['priceBand']
        change = data['change']
        series = data['series']
        faceValue=data['faceValue']
        closePrice = data['closePrice']
        open = data['open']
        lastPrice = data['lastPrice']

        GetStocksDailyData.objects.create(pricebandupper=pricebandupper,symbol=symbol, companyName=companyName,
        marketType=marketType,dayHigh=dayHigh,basePrice=basePrice,pricebandlower=pricebandlower,dayLow=dayLow,
        pChange=pChange,averagePrice=averagePrice,cm_ffm=cm_ffm,high52=high52,previousClose=previousClose,
        low52=low52,priceBand=priceBand,change=change,series=series,faceValue=faceValue,
        closePrice=closePrice,open=open,lastPrice=lastPrice)

    return redirect('/')
        
def shortViewData(request):
    AnalysedStocksData.objects.all()
    p = Paginator(AnalysedStocksData.objects.all(),15)
    page = request.GET.get('page')
    analysed_data = p.get_page(page)
    context = { 'analysed_data':analysed_data }
    return render(request, 'shortViewData.html', context)
    
def shortView(request):
    cleanTableData(AnalysedStocksData)
    
    for stock in GetStocksHistoricData.objects.values('Symbol').distinct():
        tick= (stock['Symbol']) 
        data = dataExtractor(tick)
        print (tick, data)
        time.sleep(1) 
    return redirect('/')

def stockNameCode(request):
    p = Paginator(GetStocksAngelOne.objects.filter(exch_seg= 'NSE'),10)
    page = request.GET.get('page')
    paged_data = p.get_page(page)
    context = { 'paged_data':paged_data }
    return render(request, 'stockNameCode.html', context)

def home(request):
    runDailyCheckJobs()
    p = Paginator(GetStocksAngelOne.objects.order_by('-date_created'),10)
    page = request.GET.get('page')
    paged_data = p.get_page(page)
    upgrade_orders = GetStocksAngelOne.objects.filter(exch_seg= 'NSE')
    total_orders = upgrade_orders.count()

    records = AnalysedStocksData.objects.all()
    processed_records = records.count()
    losers = {}
    gainers ={}
    try:
        losers = GetTopLosers()
        gainers = GetTopGainers()
    except Exception as ex:
        print ('Timeout Exception')
    context = { 'paged_data':paged_data, 'total_orders':total_orders, 
    'gainers':gainers,'losers':losers, 'processed_records':processed_records }
    return render(request, 'dashboard.html', context)

def allStockStore(request):
    #cleanTableData(GetStocksHistoricData)
    latest = GetLatestStocksList(GetStocksHistoricData)
    todayDate = det.today().strftime('%y-%m-%d')
    if latest == todayDate:
        print ('Latest Data Available hence skipping GetStocksHistoricData', latest, todayDate)
        pass
    else:        
        print ('Latest Data NOT Available hence gathering GetStocksHistoricData', latest, todayDate)
        present_date = date.today()
        dayData = int(getLatest())
        if dayData ==0:
            day = 180
        else:
            day = dayData
        prev_date = date.today() - timedelta(days = day)
        all_feilds = GetStocksAngelOne.objects.all()
        loop = 0
        for sym in all_feilds:
            df = get_history(symbol=sym, start=prev_date, end=present_date)
            df = (df.reset_index(drop=False))
            df['Date'] = pd.to_datetime(df['Date']).astype(str)
            df ['HighLow'] = (df['High']-df['Low']).round(2)
            df ['token'] = sym.token
            df ['PrevClose'] = (df['Prev Close'])
            df ['JumpingPercent'] = (df['HighLow'].mul(100)/df['PrevClose']).round(1)
            df ['PreClose_Close_Change'] = ( df['Close']-df['PrevClose']).round(2)
            df ['RisePercent'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1)
            df2= df[['token','Date','Symbol', 'PrevClose', 'Open', 'High','Low','Last','Close',
            'HighLow','JumpingPercent', 'PreClose_Close_Change', 'RisePercent']]
            json_list = json.loads(json.dumps(list(df2.T.to_dict().values())))
            loop = loop+1
            print (loop)
            for dic in json_list:
                GetStocksHistoricData.objects.get_or_create(**dic)
    return redirect('/')

def ViewJumpStock(request):
    p = Paginator(GetStocksHistoricData.objects.order_by('-Symbol'),20)
    page = request.GET.get('page')
    paged_data = p.get_page(page)
    context = {'paged_data':paged_data,}
    return render(request, 'jumpStock.html', context)