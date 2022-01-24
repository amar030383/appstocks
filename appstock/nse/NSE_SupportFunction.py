from nsepy import get_history
from .models import *
from datetime import date as det
from datetime import datetime as dt
import datetime, time
from datetime import timedelta
from nsetools import Nse
import requests, json, os, smtplib
import pandas as pd
nse = Nse()
   
def runDailyCheckJobs():
    times=dt.now().strftime('%d')
    day = getday()
    if  (day =='Tuesday') or (day =='Saturday'):        
        print ('The raw data collection will take place today')
    else:
        print ('The raw data collection not run today')
    
    if (times =='14') or (times =='23'):
        print ('The Angel One stock codes updates are running today')
        #getNSE_Stocks()    # Updated till 23rd Jan
        #angelOneStock()    # Updated till 23rd Jan
    else:
        print ('The  Angel One stock codes updates will not run today')

def getNSE_Stocks():
    latest = GetLatestStocksList(GetStocksList)
    todayDate = det.today().strftime('%y-%m-%d')
    if latest == todayDate:
        print ('Latest Data Available hence skipping getNSE_Stocks', latest, todayDate)
        pass
    else:        
        cleanTableData(GetStocksList)
        data = nse.get_stock_codes()
        for stock in data:
            print (stock)
            GetStocksList.objects.create(Symbol = stock) 
 
def angelOneStock():
    #cleanTableData(GetStocksAngelOne)
    latest = GetLatestStocksList(GetStocksAngelOne)
    todayDate = det.today().strftime('%y-%m-%d')
    if latest == todayDate:
        print ('Latest Data Available hence skipping angelOneStock', latest, todayDate)
        pass
    else:        
        cleanTableData(GetStocksAngelOne)
        url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
        d = requests.get(url).json()
        token_df = pd.DataFrame.from_dict(d)
        token_df['expiry'] = pd.to_datetime(token_df['expiry'])
        token_df = token_df.astype({'strike':float})
        df1 =(token_df[token_df['exch_seg']=='NSE'])
        df2= (df1[['symbol','name', 'token', 'exch_seg']]) 
        name = GetStocksList.objects.all()
        for x in name:
            nse_name_Options = x.Symbol
            stocks = [nse_name_Options+'-EQ',nse_name_Options+'-BE']
            for nseStock in stocks:
                json_list = json.loads(json.dumps(list(df2.T.to_dict().values())))
                for dic in json_list:
                    if nseStock== dic['symbol']:              
                        print ('Saving Data to DB',nseStock, dic['symbol'])
                        GetStocksAngelOne.objects.get_or_create(**dic)
            
def cleanTableData(tableName):
    print ('Cleaning table...', tableName)
    entries= tableName.objects.all()
    entries.delete()

def GetTopLosers():
    top_losers = nse.get_top_losers()
    losers = []
    for x in top_losers:
        Name = (x['symbol'])
        OpenPrice = (x['openPrice'])
        HighPrice =  (x['highPrice'])
        LowPrice =  (x['lowPrice'])
        LastTransPrice =  (x['ltp'])
        PreviousClose =  (x['previousPrice'])
        PriceDown = LastTransPrice-PreviousClose
        PercentageDown = (PriceDown*100)/OpenPrice
        PriceDown=round(PriceDown,2)
        PercentageDown=round(PercentageDown,2)
        data = {'Name':Name,'OpenPrice':OpenPrice, 'HighPrice':HighPrice, 
        'LowPrice':LowPrice, 'LastTransPrice':LastTransPrice, 
        'PreviousClose':PreviousClose, 'PriceDown':PriceDown, 
        'PercentageDown':PercentageDown}
        losers.append(data)
    return losers

def GetTopGainers(): 
    top_gainers = nse.get_top_gainers()
    gainers = []
    for x in top_gainers:
        Name =  (x['symbol'])
        OpenPrice =  (x['openPrice'])
        HighPrice =  (x['highPrice'])
        LowPrice =  (x['lowPrice'])
        LastTransPrice =  (x['ltp'])
        PreviousClose =  (x['previousPrice'])
        PriceUp = LastTransPrice-PreviousClose
        PercentageUp = (PriceUp*100)/OpenPrice
        PriceUp=round(PriceUp,2)
        PercentageUp= round(PercentageUp,2)
        data = {'Name':Name,'OpenPrice':OpenPrice, 'HighPrice':HighPrice, 
        'LowPrice':LowPrice, 'LastTransPrice':LastTransPrice, 
        'PreviousClose':PreviousClose, 'PriceUp':PriceUp, 
        'PercentageUp':PercentageUp}
        gainers.append(data)
    return gainers

def sendEmail(Subject, Message):
    g_username = os.environ.get('g_username')
    g_password = os.environ.get('g_password')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(g_username, g_password)
    msg = "\r\n".join(["From:"+g_username,"To:"+g_username, "Subject: "+Subject, Message])
    server.sendmail(g_username, g_username, msg)
    server.quit()

def dataExtractor(tick,prev_date,present_date, week):
    data = GetStocksHistoricData.objects.filter(Date__range=(prev_date, present_date)).filter(Symbol = tick)
    rise2=0
    rise3=0
    rise4=0
    rise5=0
    rise6=0
    Jump5=0
    Jump8=0
    Jump10=0
    Jump12=0
    Jump15=0
    Down1=0
    Down2=0
    Down3=0
    Down4=0
    Down5=0

    for x in data:
        RisePercent = (x.RisePercent)
        JumpingPercent = (x.JumpingPercent)

        if (RisePercent >=2) and (RisePercent <3):
            rise2+=1
        elif (RisePercent >=3) and (RisePercent <4):
            rise3+=1
        elif (RisePercent >=4) and (RisePercent <5):
            rise4+=1
        elif (RisePercent >=5) and (RisePercent <6):
            rise5+=1
        elif (RisePercent >=6):
            rise6+=1

        if (JumpingPercent >=5) and (JumpingPercent <8):
            Jump5+=1
        elif (JumpingPercent >=8) and (JumpingPercent <10):
            Jump8+=1
        elif (JumpingPercent >=10) and (JumpingPercent <12):
            Jump10+=1
        elif (JumpingPercent >=12) and (JumpingPercent <15):
            Jump12+=1
        elif (JumpingPercent >=15):
            Jump15+=1
        
        if (RisePercent <=-0) and (RisePercent >-1):
            Down1+=1
        elif (RisePercent <=-1) and (RisePercent >-2):
            Down2+=1
        elif (RisePercent <=-2) and (RisePercent >-3):
            Down3+=1
        elif (RisePercent <=-3) and (RisePercent >-4):
            Down4+=1
        elif (RisePercent <=-5):
            Down5+=1
     
    AnalysedStocksData.objects.create(Symbol = tick, Duration = week,
    rise2=rise2, rise3=rise3, rise4=rise4, rise5=rise5, rise6=rise6, 
    Jump5=Jump5, Jump8=Jump8, Jump10=Jump10, Jump12=Jump12, Jump15=Jump15, 
    Down1=Down1, Down2=Down2, Down3=Down3, Down4=Down4, Down5=Down5)

    return [week, rise2, rise3, rise4, rise5, rise6, Jump5, Jump8, Jump10, Jump12, Jump15, 
    Down1, Down2, Down3, Down4, Down5]

def getday():
    now = datetime.datetime.now()
    return (now.strftime("%A"))

def getLatest():
    try:
        data = GetStocksHistoricData.objects.latest('Date')
        last_date= (data.Date) 
        todayDate = det.today()
        days = todayDate-last_date
        return days.days
    except Exception:
        return 0

def GetLatestStocksList(database):
    try:
        data = database.objects.latest('date_created')
        date =  (data.date_created).strftime('%y-%m-%d')
        return date
    except Exception:
        return 0