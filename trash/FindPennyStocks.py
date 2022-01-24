from nsetools import Nse
import json, csv
from NSE_Info import NSE, NSE2
nse = Nse()


def get_quotes():
    file = 'All_NSE_Stock_Info.csv'
    with open(file, 'w', newline='') as csvfile:
        fields = ['pricebandupper','Token','symbol', 'companyName','marketType','dayHigh','basePrice',
        'pricebandlower','dayLow','pChange','averagePrice','cm_ffm','high52','previousClose',
        'low52','priceBand','varMargin','change','series','faceValue','closePrice','open','isinCode','lastPrice']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for stock in NSE:
            try:
                data = nse.get_quote(stock)
                row= [data['pricebandupper'],'',data['symbol'],data['companyName'],data['marketType'],
                data['dayHigh'],data['basePrice'],data['pricebandlower'],data['dayLow'],data['pChange'],
                data['averagePrice'],data['cm_ffm'],data['high52'],data['previousClose'],
                data['low52'],data['priceBand'],data['varMargin'],data['change'],data['series'],
                data['faceValue'],data['closePrice'],data['open'],data['isinCode'],data['lastPrice']]
                print (row)
                csvwriter.writerow(row)
            except Exception:
                pass
            
get_quotes()