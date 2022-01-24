from nsepy import get_history
from datetime import date, datetime, timedelta
import csv
from NSE_Info import NSE, NSE2

present_date = date.today()
prev_date = date.today() - timedelta(days = 365)

times=datetime.now().strftime('%d_%H_%M')
print (present_date, prev_date)
def informationExtractor(sym):

    df = get_history(symbol=sym, start=prev_date, end=present_date)
    df [['Symbol', 'High', 'Low', 'Open']]
    df ['HighLow'] = ( df['High']-df['Low'])
    df ['Movement %'] = (df['HighLow'].mul(100)/df['Open']).round(1) # Jump Track
    df ['MoreThan5'] = df['Movement %']>=5
    df ['MoreThan8'] = df['Movement %']>=8
    df ['MoreThan10'] = df['Movement %']>=10
    df ['MoreThan12'] = df['Movement %']>=12
    df ['MoreThan15'] = df['Movement %']>=15
    df ['MoreThan18'] = df['Movement %']>=18
    df ['MoreThan20'] = df['Movement %']>=20
    df3= (df [['High', 'Low', 'Open', 'HighLow', 'Movement %','MoreThan5','MoreThan8','MoreThan10','MoreThan12', 'MoreThan15', 'MoreThan18', 'MoreThan20']])
    return df3

def dataprocessor():
    filename = 'NSE_Circuit_Jump'+times+'.csv'
    with open(filename, 'w', newline='') as csvfile:
        fields = ['Percentage', '5%', '8%', '10%','12%','15%','18%','20%', 'Hits']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        loop = 1
        for sym in NSE2:
            print (loop, sym)
            df3 = informationExtractor(sym)
            count5 = (df3['MoreThan5']).sum()
            count8 = (df3['MoreThan8']).sum()
            count10 = (df3['MoreThan10']).sum()
            count12 = (df3['MoreThan12']).sum()
            count15 = (df3['MoreThan15']).sum()
            count18 = (df3['MoreThan18']).sum()
            count20 = (df3['MoreThan20']).sum()
            rows = [[sym, count5, count8, count10, count12, count15, count18, count20, (count5+count8+count10+count12+count15+count18+count20) ]]            
            csvwriter.writerows(rows)
            print (loop, sym,rows)          
            loop = loop+1

#dataprocessor()