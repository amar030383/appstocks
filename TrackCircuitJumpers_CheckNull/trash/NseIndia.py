import requests
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class NseIndia:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def pre_market_data(self):
        pre_market_key = {"NIFTY 50": "NIFTY", "Nifty Bank": "BANKNIFTY", "Emerge": "SME", "Securities in F&O": "FO",
                          "Others": "OTHERS", "All": "ALL"}
        key = "NIFTY 50"   # input
        data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_key[key]}", headers=self.headers).json()["data"]
        new_data = []
        for i in data:
            new_data.append(i["metadata"])
        df = pd.DataFrame(new_data)
        # return list(df['symbol'])
        return df

    def live_market_data(self):
        live_market_index = {
            'Broad Market Indices': [
                'NIFTY 50', 
                'NIFTY NEXT 50', 
                'NIFTY MIDCAP 50', 
                'NIFTY MIDCAP 100', 
                'NIFTY MIDCAP 150', 
                'NIFTY SMALLCAP 50', 
                'NIFTY SMALLCAP 100',
                'NIFTY SMALLCAP 250', 
                'NIFTY MIDSMALLCAP 400', 
                'NIFTY 100', 
                'NIFTY 200'],

            'Sectoral Indices': [
                "NIFTY AUTO", 
                "NIFTY BANK", 
                "NIFTY ENERGY", 
                "NIFTY FINANCIAL SERVICES", 
                "NIFTY FINANCIAL SERVICES 25/50", 
                "NIFTY FMCG", 
                "NIFTY IT", 
                "NIFTY MEDIA",
                "NIFTY METAL", 
                "NIFTY PHARMA", 
                "NIFTY PSU BANK", 
                "NIFTY REALTY", 
                "NIFTY PRIVATE BANK"],
            }
        

        indices = "Sectoral Indices"    # input
        key = "NIFTY FINANCIAL SERVICES 25/50"     # input
        data = self.session.get(f"https://www.nseindia.com/api/equity-stockIndices?index={live_market_index[indices][live_market_index[indices].index(key)].upper().replace(' ','%20').replace('&', '%26')}", headers=self.headers).json()["data"]
        df = pd.DataFrame(data)

        return df

    def holidays(self):
        holiday = ["clearing", "trading"]
        # key = input(f'Select option {holiday}\n: ')
        key = "trading"   # input
        data = self.session.get(f'https://www.nseindia.com/api/holiday-master?type={holiday[holiday.index(key)]}', headers=self.headers).json()
        df = pd.DataFrame(list(data.values())[0])
        return df

nse = NseIndia()

# print(nse.pre_market_data())
da=(nse.live_market_data())
print (type(da))
# print(nse.holidays())
da.to_csv('test.csv')