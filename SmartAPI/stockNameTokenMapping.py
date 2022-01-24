from elasticsearch import Elasticsearch
es = Elasticsearch()
import json, csv, datetime

from datetime import datetime
times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('NSE_BSEStockNamesCode2.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        token = row[0]
        symbol = row[1]
        name = row[2]
        exch_seg = row[3]
       
        data = {
            "Token" : token,
            "Symbol" : symbol,
            "Name" : name,
            'Category' : '',
            "Exch_seg" : exch_seg,
            "LastSavedOn" : times,
            }
        #print (data)
        print (json.dumps(data, indent = 4))
        res = es.index(index="stocknamecode",document=data)
        #print(res['result'])

