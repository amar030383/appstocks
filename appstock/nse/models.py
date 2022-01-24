from django.db import models

class GetStocksList(models.Model):          # Saves NSE stock names
    Symbol = models.CharField(max_length=15, null=True)
    Market = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    class Meta:
        ordering = ('-Symbol',)

    def __str__(self): 
        return self.Symbol

class GetStocksAngelOne(models.Model):      # Saves AngelOne Stock codes
    token = models.CharField(primary_key=True,max_length=50)
    symbol = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    exch_seg = models.CharField(max_length=10, null=True)
    category = models.CharField(max_length=500, null=True)
    tags = models.CharField(max_length=500, null=True)
    exp = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    class Meta:
        ordering = ('-name',)
    
    def __str__(self): 
        return self.name
    
class GetStocksHistoricData(models.Model):  # Saves Historic Data of 6 months
    token = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    SymName = models.CharField(max_length=50, null=True)
    Symbol = models.CharField(max_length=50, null=True)
    PrevClose = models.FloatField(null=True)
    Open = models.FloatField(null=True)
    High = models.FloatField(null=True)
    Low = models.FloatField(null=True)
    Last = models.FloatField(null=True)
    Close = models.FloatField(null=True)
    HighLow = models.FloatField(null=True)
    JumpingPercent = models.FloatField(null=True)
    PreClose_Close_Change = models.FloatField(null=True)
    RisePercent = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    class Meta:
        ordering = ('-Symbol',)

    def __str__(self): 
        return self.Symbol

class NoResultFoundStocks(models.Model):      
    token = models.IntegerField(null=True)
    symbol = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    class Meta:
        ordering = ('-symbol',)

    def __str__(self): 
        return self.symbol

class AnalysedStocksData(models.Model):     # Saves Analysed Stock data from historic data,
    Symbol = models.CharField(max_length=20, null=True)
    Duration = models.IntegerField(null=True)
    rise2 = models.IntegerField(null=True)
    rise3 = models.IntegerField(null=True)
    rise4 = models.IntegerField(null=True)
    rise5 = models.IntegerField(null=True)
    rise6 = models.IntegerField(null=True)

    Jump5 = models.IntegerField(null=True)
    Jump8 = models.IntegerField(null=True)
    Jump10 = models.IntegerField(null=True)
    Jump12 = models.IntegerField(null=True)
    Jump15 = models.IntegerField(null=True)

    Down1 = models.IntegerField(null=True)
    Down2 = models.IntegerField(null=True)
    Down3 = models.IntegerField(null=True)
    Down4 = models.IntegerField(null=True)
    Down5 = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)

    class Meta:
        ordering = ('-Symbol',)

    def __str__(self): 
        return self.Symbol

class GetStocksDailyData(models.Model):
    symbol = models.CharField(max_length=15, null=True)
    Market = models.CharField(max_length=10, null=True)
    pricebandupper = models.FloatField(null=True)
    companyName = models.CharField(max_length=100, null=True)
    marketType = models.CharField(max_length=10, null=True)
    dayHigh = models.FloatField(null=True)
    basePrice = models.FloatField(null=True)
    pricebandlower = models.FloatField(null=True)
    dayLow = models.FloatField(null=True)
    pChange = models.FloatField(null=True)
    averagePrice = models.FloatField(null=True)
    cm_ffm = models.FloatField(null=True)
    high52 = models.FloatField(null=True)
    previousClose = models.FloatField(null=True)
    low52 = models.FloatField(null=True)
    priceBand = models.CharField(max_length=20, null=True)
    change = models.FloatField(null=True)
    series = models.CharField(max_length=10, null=True)
    faceValue = models.FloatField(null=True)
    closePrice = models.FloatField(null=True)
    open = models.FloatField(null=True)
    lastPrice = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    class Meta:
        ordering = ('-symbol',)

    def __str__(self): 
        return self.symbol


































# class JumpStock(models.Model):
#     id = models.AutoField(primary_key=True)
#     Name = models.CharField(max_length=50, null=True)
#     months = models.IntegerField(null=True)
#     jump5 = models.IntegerField(null=True)
#     jump8 = models.IntegerField(null=True)
#     jump10 = models.IntegerField(null=True)
#     jump12 = models.IntegerField(null=True)
#     jump15 = models.IntegerField(null=True)
#     jump18 = models.IntegerField(null=True)
#     jump20 = models.IntegerField(null=True)
#     count2 = models.IntegerField(null=True)
#     count3 = models.IntegerField(null=True)
#     count4 = models.IntegerField(null=True)
#     count5 = models.IntegerField(null=True)
#     count6 = models.IntegerField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    
#     def __str__(self): 
#         return self.id

# class ShortListedStocks(models.Model): # Saves AngelOne Stock codes for usage
#     token = models.CharField(primary_key=True,max_length=50)
#     stock_Name = models.CharField(max_length=50, null=True)
#     Name = models.CharField(max_length=50, null=True)
#     Market = models.CharField(max_length=10, null=True)
#     Category = models.CharField(max_length=50, null=True)
#     tags = models.CharField(max_length=500, null=True)
#     trend = models.CharField(max_length=50, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    
#     def __str__(self): 
#         return self.token
