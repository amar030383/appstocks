from nsetools import Nse
nse = Nse()
def topGainers():
    top_gainers = nse.get_top_gainers()
    data = []
    for x in top_gainers:
        Name =  (x['symbol'])
        OpenPrice =  (x['openPrice'])
        HighPrice =  (x['highPrice'])
        LowPrice =  (x['lowPrice'])
        LastTransPrice =  (x['ltp'])
        PreviousClose =  (x['previousPrice'])
        PriceUp = LastTransPrice-PreviousClose
        PercentageUp = (PriceUp*100)/OpenPrice
        result = Name,OpenPrice, HighPrice, LowPrice, LastTransPrice, PreviousClose, round(PriceUp, 2), round(PercentageUp, 2)
        print (result)
        data.append(result)
    return (data)


def topLoosers():
    top_gainers = nse.get_top_losers()
    data = []
    for x in top_gainers:
        Name =  (x['symbol'])
        OpenPrice =  (x['openPrice'])
        HighPrice =  (x['highPrice'])
        LowPrice =  (x['lowPrice'])
        LastTransPrice =  (x['ltp'])
        PreviousClose =  (x['previousPrice'])
        PriceDown = LastTransPrice-PreviousClose
        PercentageDown = (PriceDown*100)/OpenPrice
        result = Name,OpenPrice, HighPrice, LowPrice, LastTransPrice, PreviousClose, round(PriceDown, 2), round(PercentageDown, 2)
        print (result)
        data.append(result)
    return (data)

topLoosers()
#topGainers()    