from nsepy import get_history
import pandas as pd
from datetime import date

def informationExtractor(sym):
    df = get_history(symbol=sym, start=date(2021,12,28), end=date(2021,12,31))
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

symbol=['RAIN', 'IBULHSGFIN']

#with pd.ExcelWriter('All_Stocks.xlsx') as writer1:
for sym in symbol:
    df3 = informationExtractor(sym)
    df4 = (df3['MoreThan4']).count()
    print (df4)