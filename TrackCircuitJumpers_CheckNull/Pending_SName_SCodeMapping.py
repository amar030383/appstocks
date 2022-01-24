import pdb; 
import requests, csv
from NSE_Info import index
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; ''x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
cookies = response.cookies
loop = 1

filename ="Category.csv"
f = open(filename, 'a', newline='')
writer = csv.writer(f)
OS_fields = ['StockCode','StockName', 'Name', 'Market','sindex']

writer.writerow(OS_fields)

for sindex in index:
    ind = (sindex.replace(" ", "%20"))
    url = main_url+"/api/equity-stockIndices?index="+ind
    try:
        resp = requests.get(url, headers=headers, cookies=cookies)
        json_resp = resp.json()
        data =  (json_resp['data'])
        st = []
        for x in data:
            st.append(x['symbol'])
        
        with open('NSE_BSEStockNamesCode.csv') as f:
            readCSV = csv.reader(f, delimiter=',')
            for row in readCSV:
                StockCode = row[0]
                StockName  = row[1]
                Name = row[2]
                Market = row[3]
                if Name in st:
                    print (loop, StockCode,StockName, Name, Market,sindex)
                    rows= [[StockCode,StockName, Name, Market,sindex]]
                    writer.writerows(rows)
                loop+=1

    except Exception:
        pass