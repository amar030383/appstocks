from nsetools import Nse
nse = Nse() 
data = nse.get_stock_codes()
loop = 0
for x in data:
    
    loop+=1
    print (loop, x)
#    with open('NSE_Stocks.txt', 'a') as f:
 #       f.writelines('"'+x+'",')
 #       f.writelines('\n')