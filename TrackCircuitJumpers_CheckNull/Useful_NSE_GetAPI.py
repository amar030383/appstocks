import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; ''x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
cookies = response.cookies



preopen_market_url = "https://www.nseindia.com/api/market-data-pre-open?key=NIFTY"
preopen_data = requests.get(preopen_market_url, headers=headers, cookies=cookies)
print("Pre-open market data", preopen_data.text)


url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
nifty_50_data = requests.get(url, headers=headers, cookies=cookies)
nifty50_data = nifty_50_data.json()

ohl_buy_stocks = []
ohl_sell_stocks = []

for stocks in nifty50_data.get("data"):
    if stocks['open'] == stocks['dayLow']:
        ohl_buy_stocks.append(stocks['symbol'])

    if stocks['open'] == stocks['dayHigh']:
        ohl_sell_stocks.append(stocks['symbol'])


print("Most Probable buying Stocks based on OHL Strategy", ohl_buy_stocks)
print("Most Probable Selling Stocks based on OHL Strategy", ohl_sell_stocks)
