from nsepy import get_history
import pandas as pd
from datetime import date

filename = 'PercentageData.xlsx'

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

def multiple_dfs(df_list, sheets, file_name, spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')   
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)   
        row = row + len(dataframe.index) + spaces + 1
    writer.save()

symbol=['RAIN', 'IBULHSGFIN']
#symbol=['RAIN']
with pd.ExcelWriter('mult_sheets_1.xlsx') as writer1:
    for sym in symbol:
        df3 = informationExtractor(sym)
        count5 = (df3['MoreThan5']).sum()
        count8 = (df3['MoreThan8']).sum()
        count10 = (df3['MoreThan10']).sum()
        sheetname = sym+'_'+str(count5)+'_'+str(count8)+'_'+str(count10)
        df3.to_excel(writer1, sheet_name = sheetname)
