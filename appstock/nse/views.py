from calendar import week
from django.http import response
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from nse.NSE_SupportFunction import *
import json, time
from datetime import date, timedelta

def stockHomeAnalysis(request):
    all_data = AnalysedStocksData.objects.all()

    week = []
    for x in all_data:
        if (x.Duration==8)&(x.rise4>=20):  
            output = {'Symbol':x.Symbol, 'Duration':x.Duration,"rise3":x.rise3,"rise4":round(x.rise4), "rise5":x.rise5,
            "Down1":x.Down1,"Down2": x.Down2, "Down3":x.Down3, "Down4":x.Down4,"Down5":x.Down5}
            week.append(output)
    context = {'data' : week}
    return render(request, 'stockHomeAnalysis.html', context)

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
    p = Paginator(AnalysedStocksData.objects.all(),15)
    page = request.GET.get('page')
    analysed_data = p.get_page(page)
    context = { 'analysed_data':analysed_data }
    return render(request, 'shortViewData.html', context)
    
def shortView(request):
    cleanTableData(AnalysedStocksData)
    present_date = det.today()
    weeks = [1,2,4,8,12,16,20,24]
    for week in weeks:
        day = (week*7)
        prev_date = present_date - timedelta(days = day)
        for stock in GetStocksHistoricData.objects.values('Symbol').distinct():
            tick= (stock['Symbol']) 
            data = dataExtractor(tick,prev_date,present_date, week)
            print (tick, data)
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

def getAllHistoricData():
    historic = GetStocksHistoricData.objects.order_by().values_list('Symbol').distinct()
    capturedHistoric=[]
    for x in historic:
        AlreadyHistoric =  ''.join(x)
        capturedHistoric.append(AlreadyHistoric)
    return capturedHistoric

def allStockStore(request):
    loop = 0   
    dataNotFound = []     
    present_date = date.today()  
    prev_date = present_date - timedelta(days = 180)

    #cleanTableData(GetStocksHistoricData)
    capturedHistoric = getAllHistoricData()
    all_feilds = GetStocksAngelOne.objects.all()
    for data in all_feilds:
        sym= data.symbol
        nam = data.name
        toke = data.token
        if nam in capturedHistoric: 
            print ('Escaping ', nam)           
            pass
        else:
            df = get_history(symbol=nam, start=prev_date, end=present_date)
            df = (df.reset_index(drop=False))
            df['Date'] = pd.to_datetime(df['Date']).astype(str)
            df ['HighLow'] = (df['High']-df['Low']).round(2)
            df ['token'] = toke
            df ['SymName'] = sym
            df ['PrevClose'] = (df['Prev Close'])
            df ['JumpingPercent'] = (df['HighLow'].mul(100)/df['PrevClose']).round(1)
            df ['PreClose_Close_Change'] = ( df['Close']-df['PrevClose']).round(2)
            df ['RisePercent'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1)
            
            df2= df[['token','Date','SymName','Symbol', 'PrevClose', 'Open', 'High','Low','Last','Close',
            'HighLow','JumpingPercent', 'PreClose_Close_Change', 'RisePercent']]

            if df2.empty:
                dataNotFound.append(NoResultFoundStocks(token=toke, symbol=sym,name=nam))
            else:
                json_list = json.loads(json.dumps(list(df2.T.to_dict().values())))
                bulksave = []
                for dic in json_list:
                    toke=dic['token']
                    Dat =dic['Date']
                    SymNam=dic['SymName']
                    Symbo=dic['Symbol']
                    PrevClos=dic['PrevClose']
                    Ope=dic['Open']
                    Hig =dic['High']
                    Lo =dic['Low']
                    Las =dic['Last']
                    Clos =dic['Close']
                    HighLo=dic['HighLow']
                    JumpingPercen=dic['JumpingPercent']
                    PreClose_Close_Chang =dic['PreClose_Close_Change']
                    RisePercen =dic['RisePercent']
                    bulksave.append(GetStocksHistoricData(token=toke, Date=Dat, 
                    SymName=SymNam,Symbol=Symbo,PrevClose=PrevClos,Open=Ope,
                    High=Hig,Low=Lo,Last=Las,Close=Clos,HighLow=HighLo,
                    JumpingPercent=JumpingPercen,PreClose_Close_Change=PreClose_Close_Chang,
                    RisePercent=RisePercen))
                GetStocksHistoricData.objects.bulk_create(bulksave)
            loop = loop+1
            print (loop,sym)

    cleanTableData(NoResultFoundStocks)
    NoResultFoundStocks.objects.bulk_create(dataNotFound)
    return redirect('/')















def ViewJumpStock(request):
    p = Paginator(GetStocksHistoricData.objects.order_by('-Symbol'),20)
    page = request.GET.get('page')
    paged_data = p.get_page(page)
    context = {'paged_data':paged_data,}
    return render(request, 'jumpStock.html', context)