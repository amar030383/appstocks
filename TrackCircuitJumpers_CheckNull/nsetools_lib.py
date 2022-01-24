from nsetools import Nse
import json
from NSE_Info import NSE, NSE2
nse = Nse()
#data = nse.get_index_list()
#data = nse.get_quote('upl')
#print (data)
#print (json.dumps(data, indent = 2))


def get_quotes():
    data = nse.get_quote('upl')
    #print (data)
    print (json.dumps(data, indent = 2))

for stock in NSE2:
    data = nse.get_quote(stock)
    print (json.dumps(data, indent = 2))
    

    

