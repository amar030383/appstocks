from nsepy import get_history

from datetime import date
import csv
from NSE_Info import NSE, NSE2

def informationExtractor(sym):
    df = get_history(symbol=sym, start=date(2021,1,1), end=date(2021,12,31))
    df [['Symbol', 'Prev Close', 'Close']]
    df ['PreClose_Close_Change'] = ( df['Close']-df['Prev Close'])
    df3 = df ['Movement %'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1)

    df ['MoreThan2'] = df['Movement %']>=2
    df ['MoreThan3'] = df['Movement %']>=3
    df ['MoreThan4'] = df['Movement %']>=4
    df ['MoreThan5'] = df['Movement %']>=5
    df ['MoreThan6'] = df['Movement %']>=6
    df3= (df [['Symbol','Open', 'Prev Close', 'Close','PreClose_Close_Change', 'Movement %','MoreThan2','MoreThan3','MoreThan4','MoreThan5','MoreThan6']])
    return df3

def dataprocessor():
    filename = 'NSE_Circuit_Jump.csv'
    with open(filename, 'w', newline='') as csvfile:
        fields = ['Percentage', '2%', '3%','4%','5%','6%']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        loop = 1
        for sym in NSE:
            print (loop, sym)
            df3 = informationExtractor(sym)
            count2 = (df3['MoreThan2']).sum()
            count3 = (df3['MoreThan3']).sum()
            count4 = (df3['MoreThan4']).sum()
            count5 = (df3['MoreThan5']).sum()
            count6 = (df3['MoreThan6']).sum()
            rows = [[sym, count2, count3, count4, count5, count6]]            
            csvwriter.writerows(rows)
            loop = loop+1

dataprocessor()
