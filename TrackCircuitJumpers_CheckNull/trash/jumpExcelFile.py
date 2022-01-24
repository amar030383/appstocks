from nsepy import get_history
from datetime import date
import csv

def informationExtractor(sym):
    df = get_history(symbol=sym, start=date(2021,1,1), end=date(2021,12,31))
    df [['Symbol', 'High', 'Low', 'Open']]
    df ['HighLow'] = ( df['High']-df['Low'])
    df ['Movement %'] = (df['HighLow'].mul(100)/df['Open']).round(1)
    df ['MoreThan4'] = df['Movement %']>=4
    df ['MoreThan5'] = df['Movement %']>=5
    df ['MoreThan8'] = df['Movement %']>=8
    df ['MoreThan10'] = df['Movement %']>=10
    df ['MoreThan12'] = df['Movement %']>=12
    df3= (df [['High', 'Low', 'Open', 'HighLow', 'Movement %', 'MoreThan4','MoreThan5','MoreThan8','MoreThan10','MoreThan12']])
    return df3

def dataprocessor():
    filename = 'NSE_Jump_Data.csv'
    symbol=['RAIN', 'IBULHSGFIN', 'TCS', 'UPL']
    with open(filename, 'w', newline='') as csvfile:
        fields = ['Percentage', '4%', '5%', '8%', '10%','12%', 'Hits']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for sym in symbol:
            df3 = informationExtractor(sym)
            count4 = (df3['MoreThan4']).sum()
            count5 = (df3['MoreThan5']).sum()
            count8 = (df3['MoreThan8']).sum()
            count10 = (df3['MoreThan10']).sum()
            count12 = (df3['MoreThan12']).sum()
            rows = [[sym, count4, count5, count8, count10, count12, (count4+ count5+ count8+ count10+count12) ]]            
            csvwriter.writerows(rows)

dataprocessor()