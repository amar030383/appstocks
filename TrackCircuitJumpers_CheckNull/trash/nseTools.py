from nsetools import Nse
nse = Nse()
#q = nse.get_quote('RAIN') 
data = nse.get_stock_codes()
for x in data:
    with open('NSE_Stocks.txt', 'a') as f:
        f.writelines('"'+x+'",')
        f.writelines('\n')