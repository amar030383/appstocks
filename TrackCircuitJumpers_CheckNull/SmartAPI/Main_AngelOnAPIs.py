from smartapi import SmartWebSocket
from connectToken import builtConnection
import os, json
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

def placeOrder(tradingsymbol, symboltoken, price):
    try:
        orderparams = { 
            "variety": "NORMAL", "tradingsymbol": tradingsymbol, "symboltoken": symboltoken, "transactiontype": "BUY",
            "exchange": "NSE",  "ordertype": "LIMIT", "producttype": "DELIVERY", "duration": "DAY","price": price, "quantity": "1"
            }
        orderId=obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e.message))

def webSocket(feedToken):
    FEED_TOKEN=feedToken
    CLIENT_CODE=os.environ.get('angel_username')
    token="nse_cm|15337"    #   SAMPLE: nse_cm|2885&nse_cm|1594&nse_cm|11536&nse_cm|3045
    task="mw"              
    ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

    def on_message(ws, message1):
        message = (message1[0])
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

#placeOrder(tradingsymbol, symboltoken, price)
webSocket(feedToken)