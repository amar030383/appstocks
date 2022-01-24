from datetime import datetime
times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
from elasticsearch import Elasticsearch
es = Elasticsearch()
import json
data = {
        "ap" : "244.87",
        "bp" : "245.60",
        "bq" : "111",
        "bs" : "190",
        "c" : "245.00",
        "cng" : "00.85",
        "Market" : "nse_cm",
        "lo" : "243.20",
        "LastTranPrice" : "244.85",
        "LastTranQuant" : "37",
        "LastSavedOn" : times,
        "name" : "sf",
        "nc" : "00.3469",
        "sp" : "245.80",
        "tbq" : "270233",
        "StockCode" : "15337",
        "to" : "188827582.58",
        "tsq" : "513766",
        "v" : "771134",
        }

print (json.dumps(data, indent = 4))
res = es.index(index="stockmarketdata",document=data)
print(res['result'])
