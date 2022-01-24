from nsepy import get_history
from NSE_Info import NSE, NSE2, NSE3
from datetime import date, timedelta,datetime
import csv
present_date = date.today()
prev_date = date.today() - timedelta(days = 10)
times=datetime.now().strftime('%d_%H_%M')

def informationExtractor(sym):
    df = get_history(symbol=sym, start=prev_date, end=present_date)
    df ['PreClose_Close_Change'] = ( df['Close']-df['Prev Close'])
    df3 = df ['Movement %'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1)
    df ['MoreThan2'] = df['Movement %']>=2
    df ['MoreThan3'] = df['Movement %']>=3
    df3= (df [['Symbol','Open', 'Prev Close', 'Close','PreClose_Close_Change', 'Movement %','MoreThan2','MoreThan3']])
    return df3

def dataprocessor():
    filename = 'NSE_Circuit_Jump'+times+'.csv'
    with open(filename, 'w', newline='') as csvfile:
        fields = ['Percentage', '2%', '3%']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        loop = 1
        for sym in NSE2:
            print (loop, sym)
            df3 = informationExtractor(sym)
            count2 = (df3['MoreThan2']).sum()
            count3 = (df3['MoreThan3']).sum()
            count = count2-count3
            rows = [[sym, count, count3]]            
            csvwriter.writerows(rows)
            loop = loop+1
            

dataprocessor()
