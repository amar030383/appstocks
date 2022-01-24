from smartapi import SmartWebSocket
from connectToken import builtConnection
import os, json, csv, time
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
resp = builtConnection()
obj= (resp[0])
feedToken = (resp[3])

tradingsymbol="RAIN-EQ"
symboltoken = "15337"
price = "240"
quantity=1


def webSocket(feedToken):
    FEED_TOKEN=feedToken
    CLIENT_CODE=os.environ.get('angel_username')
    
    #token="nse_cm|30125"    #   SAMPLE: nse_cm|2885&nse_cm|1594&nse_cm|11536&nse_cm|3045
    token="nse_cm|"+symboltoken+"&nse_cm|30125"    #   SAMPLE: nse_cm|2885&nse_cm|1594&nse_cm|11536&nse_cm|3045
    print (token)
    task="mw"              
    ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

    def on_message(ws, message1):
        message = (message1[0])
        print (message)
        
        try:
            if  message['ap']:
                data = {
                        "bp" : message['bp'],
                        'bq' : message['bq'],
                        'bs' : message['bs'],
                        'c' : message['c'],
                        'cng' : message['cng'],
                        'Market' : message['e'],
                        'lo' : message['lo'],
                        'LastTranPrice' : message['ltp'],
                        'LastTranQuant' : message['ltq'],
                        'LastTranTime' : message['ltt'],
                        'name' : message['name'],
                        'nc' : message['nc'],
                        'sp' : message['sp'],
                        'StockCode' : message['tk'],        
                    }
                #print (json.dumps(data, indent = 4))
                res = es.index(index="stockmarketdata", doc_type='share',document=data)
                print(res['result'])
        except Exception as e:
            pass
        
        
    def on_open(ws):
        ss.subscribe(task,token)
        
    def on_error(ws, error):
        pass
        
    def on_close(ws):
        print("Close")

    ss._on_open = on_open
    ss._on_message = on_message
    ss._on_error = on_error
    ss._on_close = on_close
    ss.connect()

def placeOrderLimit(tradingsymbol, symboltoken, price, quantity):
    try:
        orderparams = { 
            "variety": "NORMAL", "tradingsymbol": tradingsymbol, "symboltoken": symboltoken, "transactiontype": "BUY",
            "exchange": "NSE",  "ordertype": "LIMIT", "producttype": "DELIVERY", "duration": "DAY","price": price, "quantity": quantity
            }
        orderId=obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e.message))

def placeOrderMarket(tradingsymbol, symboltoken, quantity):
    try:
        orderparams = { 
            "variety": "NORMAL", "tradingsymbol": tradingsymbol, "symboltoken": symboltoken, "transactiontype": "BUY",
            "exchange": "NSE",  "ordertype": "MARKET", "producttype": "DELIVERY", "duration": "DAY", "quantity": quantity
            }
        orderId=obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e.message))

def executeOrdersMarket():
    file2 = ('IdentifiedStocks2.csv')
    with open(file2,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            Token = row[0]
            shareName = row[1]
            quantity = 1
            placeOrderMarket(shareName, Token, quantity)
            time.sleep(2)

webSocket(feedToken)
#executeOrdersMarket()
#placeOrderMarket(tradingsymbol, symboltoken, quantity)

