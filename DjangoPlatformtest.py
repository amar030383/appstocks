import csv
from nsepy import get_history
from datetime import date, datetime, timedelta
from NSE_Info import NSE, NSE2
import pandas as pd
import json, requests, time

def informationExtractor(prev_date,present_date):
    for sym in NSE2:
        df = get_history(symbol=sym, start=prev_date, end=present_date)   
        df = (df.reset_index(drop=False))
        df['Date'] = pd.to_datetime(df['Date']).astype(str)
        df ['HighLow'] = (df['High']-df['Low']).round(2)
        df ['Jumping%'] = (df['HighLow'].mul(100)/df['Prev Close']).round(1) # Jump Track
        df ['PreClose_Close_Change'] = ( df['Close']-df['Prev Close']).round(2)
        df ['Rise%'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1) 
        df2= df[['Date','Symbol', 'Prev Close', 'Open', 'High','Low','Last','Close',
        'HighLow','Jumping%', 'PreClose_Close_Change', 'Rise%']]
        json_list = json.loads(json.dumps(list(df2.T.to_dict().values())))
        for dic in json_list:
            print (dic)
            time.sleep(30)
            
def start():
    present_date = date.today()
    weeks = [4]
    for week in weeks:
        days = (week*7)
        times=datetime.now().strftime('%d_%H_%M')
        prev_date = date.today() - timedelta(days = days)
        filename = 'NSE_Circuit_'+str(week)+'_Week_'+times
        informationExtractor(prev_date,present_date)


start()

