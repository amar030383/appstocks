from datetime import datetime
import requests
from datetime import date, datetime, timedelta
import pandas as pd


def weekConvertor():
    weeks = [1,2,4,8]
    for week in weeks:
        day = (week*7)
        prev_date = date.today() - timedelta(days = day)
        print (prev_date)
      
      


def runDailyCheckJobs():
    times=datetime.now().strftime('%d')
    if (times =='17') or (times =='16'):
        print ('The jobs are running today')
    else:
        print ('The jobs will not run today')

def angelOneStock():
    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    d = requests.get(url).json()
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry'])
    token_df = token_df.astype({'strike':float})
    df1 =(token_df[(token_df['exch_seg']=='NSE')|(token_df['exch_seg']=='BSE')])
    df4= (df1[['symbol','name', 'token', 'exch_seg']])
    
def getday():
    import datetime
    now = datetime.datetime.now()
    return (now.strftime("%A"))

weekConvertor()