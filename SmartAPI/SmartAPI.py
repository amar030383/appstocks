import http.client, json, os
conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
username = os.environ.get('angel_username')
password = os.environ.get('angel_password')
api_key = os.environ.get('angel_api')
payload = ''

def generateToken():
    payload = {"clientcode":username,"password":password}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-UserType': 'USER','X-SourceID': 'WEB', 
    'X-ClientLocalIP': '192.168.29.25','X-ClientPublicIP': '49.37.76.50','X-MACAddress': '68-3E-26-1F-C5-D8', 'X-PrivateKey': api_key }
    json_data = json.dumps(payload)
    conn.request("POST","/rest/auth/angelbroking/user/v1/loginByPassword",json_data,headers)
    res = conn.getresponse()
    data = res.read()
    f= data.decode("utf-8")
    res = json.loads(f)
    jwtToken=(res['data']['jwtToken'])    
    return [jwtToken]

def getTokenHeader():
    data = generateToken()
    headers = {
    'Authorization': 'Bearer '+data[0],'Content-Type': 'application/json','Accept': 'application/json', 
    'X-UserType': 'USER','X-SourceID': 'WEB', 'X-ClientLocalIP': '192.168.29.25','X-ClientPublicIP': '49.37.76.50',
    'X-MACAddress': '68-3E-26-1F-C5-D8','X-PrivateKey': api_key
    }
    return headers

def processData(res):
    data = res.read()
    f=(data.decode("utf-8"))
    res = json.loads(f)
    dara=(res['data']) 
    return dara

def getTradeBook():     # Today's Executed Stocks
    headers = getTokenHeader()
    conn.request("GET", "/rest/secure/angelbroking/order/v1/getTradeBook", payload, headers)
    res = conn.getresponse()
    output = processData(res)
    print (output)
    
def getPortfolio():
    headers = getTokenHeader()
    conn.request("GET", "/rest/secure/angelbroking/portfolio/v1/getHolding", payload, headers)
    res = conn.getresponse()
    output = processData(res)
    portfolio = []
    for d in output:
        #print (d)
        if 'RAILTEL-EQ' == (d['tradingsymbol']) :       
            tradingsymbol = (d['tradingsymbol'])
            isin = (d['isin']) 
            t1quantity = d['t1quantity']
            quantity= (d['quantity'])
            averageprice = (d['averageprice'])
            ltp = (d['ltp'])
            symboltoken = (d['symboltoken'])
            close = d['close']
            total_investment = round(averageprice*quantity)
            current_value = round(quantity*ltp)
            profit_loss = round(current_value-total_investment)
            perc_profit_loss = (total_investment/profit_loss)
            stocks=[tradingsymbol,quantity, total_investment, current_value,ltp, profit_loss, round (perc_profit_loss, 2)]
            print (stocks)
    
getPortfolio()